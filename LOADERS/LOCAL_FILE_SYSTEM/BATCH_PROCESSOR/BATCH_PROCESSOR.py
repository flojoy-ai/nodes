from flojoy import flojoy, Vector, Scalar, SmallMemory, DefaultParams
import numpy as np
import glob
from typing import Any

memory_key = "batch-processor-info"


def get_fnames(d, p):
    return [file for file in glob.glob(d+'/'+p, recursive=True)]

@flojoy(inject_node_metadata=True)
def BATCH_PROCESSOR(
    current_iteration: Scalar,
    default_params: DefaultParams,
    directory_path: str,
    pattern: str = "",
    refresh: bool = True, 
) -> Vector:
    #=======================================================
    # At first iteration, we want to identify the initial 
    # sources to iterate over. Also at the first iteration,
    # we want to write the initial list of files to SmallMemory.
    # What we'll do after is to then load the list from
    # SmallMemory, pop front the next item, and rewrite the 
    # popped list to SmallMemory. If the refresh parameter
    # is toggled, we will re-search the glob pattern, find new
    # entries, and append them to the array in SmallMemory.
    #
    # if iteration #1: 
    #      Pattern find
    #      Write to Small Memory
    # if refresh:
    #      glob again
    #      Read from SmallMemory
    #      Find difference between
    #      Append to array to write to SmallMemory
    # Read from Small memory
    # Pop array
    # Write to SmallMemory
    # return popped string as Vec<str>
    #=======================================================
    node_id = default_params.node_id
    curr_iter = int(current_iteration.c[0])
    # if iteration 1, pattern find, then write to SmallMemory
    if curr_iter == 1: #loop index starts at 1, sigh
        files = get_fnames(directory_path, pattern if pattern else '*')
        SmallMemory().write_to_memory(
            node_id, 
            memory_key, 
            {
                'node_id' : node_id,
                'current_iteration' : curr_iter,
                'files' : files
            }
        )
    # if refresh, glob again, read from smallmemory, 
    # find difference, append difference to files in SmallMemory
    if refresh:
        new_files = get_fnames(directory_path, pattern if pattern else '*')
        old_data: dict[str, Any] = SmallMemory().read_memory(node_id, memory_key) or {}
        old_files = old_data['files']
        if old_data:
            difference = set(new_files).difference(set(old_files)) #designed to only catch the addition of files
            if difference:
                # this means there are more new files added to the mix
                SmallMemory().write_to_memory(
                    node_id, 
                    memory_key, 
                    {
                        'node_id' : node_id,
                        'current_iteration' : curr_iter,
                        'files' : files+list(difference)
                    }
                )
    # Now we read from SmallMemory and pop fname
    data: dict[str, Any] = SmallMemory().read_memory(node_id, memory_key) or {}
    fname = data['files'].pop(0)
    # Now write to SmallMemory for the next iteration
    data['current_iteration'] = curr_iter
    SmallMemory().write_to_memory(node_id,memory_key, data)
    #And return the current fname
    return Vector(
        v=np.array(fname)[...,np.newaxis]
    )

