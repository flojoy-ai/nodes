from flojoy import flojoy, Scalar, SmallMemory, DefaultParams, TextBlob
import glob
from typing import Any, TypedDict

memory_key = "batch-processor-info"

class BATCH_OUTPUT(TypedDict):
    fname: TextBlob
    n_files: Scalar

def get_fnames(d, p):
    return [file for file in glob.glob(d+'/'+p, recursive=True)]

@flojoy(inject_node_metadata=True)
def BATCH_PROCESSOR(
    current_iteration: Scalar,
    default_params: DefaultParams,
    directory_path: str,
    pattern: str = "",
    refresh: bool = True, 
) -> BATCH_OUTPUT:
    """
    This node is designed to glob match a pattern in the given input directory.

    From here, in conjunction with a loop, we iterate
    over all the files found, and return each one by
    file path as a TextBlob. The TextBlob can be recognized as 
    an optional input to the `LOCAL_FILE` node, which can
    then load the file at that path and return the appropriate
    datatype.

    Parameters
    ----------
    current_iteration       :       Scalar
        This is the input from the `LOOP_INDEX` node that determines
        if we need to initialize this routine or not.
    default_params          :       DefaultParams
        This provides the node_id so that we can identify which
        object in SmallMemory to pull (for example, unique identification
        of this node if there are multiple BATCH_PROCESSOR nodes)
    directory_path          :       str
        The directory in which we should pattern match to find the files
    pattern                 :       str
        The glob pattern to match. If not provided, all files in the directory
        are returned. The current implementation supports recursion and double
        wildcard matching.
    refresh                 :       bool
        A switching parameter that refreshes the cache of files. If a separate
        programme is expected to continuously write new files of interest to the
        directory, this flag will enable the update of the new files for processing.

    Returns
    -------
    retval                  :       TextBlob
        A `TextBlob` data container to pass to other nodes for processing

    """
    
    node_id = default_params.node_id
    curr_iter = int(current_iteration.c[0])
    # if iteration 1, pattern find, then write to SmallMemory
    if curr_iter < 2:
        files = get_fnames(directory_path, pattern if pattern else '*')
        return BATCH_OUTPUT(fname=TextBlob(text_blob=""), n_files=Scalar(c=len(files)+2))
    elif curr_iter == 2: #loop index starts at 1, sigh
        files = get_fnames(directory_path, pattern if pattern else '*')
        SmallMemory().write_to_memory(
            node_id, 
            memory_key, 
            {
                'node_id' : node_id,
                'current_iteration' : curr_iter,
                'files' : files,
                'original_files' : files
            }
        )
    # if refresh, glob again, read from smallmemory, 
    # find difference, append difference to files in SmallMemory
    if refresh:
        new_files = get_fnames(directory_path, pattern if pattern else '*')
        old_data: dict[str, Any] = SmallMemory().read_memory(node_id, memory_key) or {}
        if old_data:
            difference = set(new_files).difference(set(old_data['original_files'])) #designed to only catch the addition of files
            if not all([not d in old_data['original_files'] for d in list(difference)]):
                # this means there are more new files added to the mix
                SmallMemory().write_to_memory(
                    node_id, 
                    memory_key, 
                    {
                        'node_id' : node_id,
                        'current_iteration' : curr_iter,
                        'files' : old_data['files']+list(difference),
                        'original_files' : old_data['original_files']
                    }
                )
                
    # Now we read from SmallMemory and pop fname
    data: dict[str, Any] = SmallMemory().read_memory(node_id, memory_key) or {}
    fname = data['files'].pop(0)
    # Now write to SmallMemory for the next iteration
    data['current_iteration'] = curr_iter
    SmallMemory().write_to_memory(node_id,memory_key, data)
    #And return the current fname
    return BATCH_OUTPUT(fname = TextBlob(text_blob=fname), n_files=Scalar(c=len(data['original_files'])))

