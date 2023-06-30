from flojoy import DataContainer, DefaultParams, JobResultBuilder, flojoy #type:ignore
from typing import Any


@flojoy
def GOTO(
    default: DataContainer, default_parmas: DefaultParams, goto_node_id: str = ""
) -> dict[str, Any]:
    next_nodes = [goto_node_id] if goto_node_id != "" else []
    return JobResultBuilder().from_inputs([default]).flow_to_nodes(next_nodes).build()
