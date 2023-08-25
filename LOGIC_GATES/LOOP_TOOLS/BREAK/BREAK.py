from flojoy import flojoy, DataContainer, SmallMemory, NodeReference
from typing import Optional, Any

memory_key = "loop-info"

@flojoy
def BREAK(
    referred_node: NodeReference,
    default: Optional[DataContainer] = None,
) -> DataContainer:
    # this is the loop ID we want to break
    original_data: dict[str, Any] = SmallMemory().read_memory(referred_node.ref, memory_key) 
    data = original_data.copy()
    data['num_loop'] = 1
    data['current_iteration'] = 1
    data['is_finished'] = True
    SmallMemory().write_to_memory(referred_node.ref, memory_key, data)
    return default
