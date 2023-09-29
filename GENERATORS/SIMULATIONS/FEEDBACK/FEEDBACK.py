from typing import Optional, Any
from flojoy import (
    flojoy,
    DataContainer,
    get_job_result,
    NodeReference,
    JobResultBuilder,
)


@flojoy
def FEEDBACK(
    referred_node: NodeReference,
    default: Optional[DataContainer] = None,
) -> Any:
    """The FEEDBACK node captures the result of the specified node ID. If the result is not found, it passes the result of the parent node.

    Parameters
    ----------
    referred_node : str
        The node ID to capture the result from.
    """

    result = get_job_result(referred_node.ref)
    if result:
        return result
    else:
        return (
            JobResultBuilder()
            .from_inputs([default] if default else [])
            .flow_to_directions(["default"])
            .build()
        )
