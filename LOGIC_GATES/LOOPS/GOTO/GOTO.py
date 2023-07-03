from flojoy import DataContainer, JobResultBuilder, flojoy, ParameterTypes
from typing import Any


@flojoy
def GOTO(default: DataContainer, goto_node_id: ParameterTypes.NODE_REFERENCE = ""):
    next_nodes = [goto_node_id] if goto_node_id != "" else []
    return JobResultBuilder().from_inputs([default]).flow_to_nodes(next_nodes).build()
