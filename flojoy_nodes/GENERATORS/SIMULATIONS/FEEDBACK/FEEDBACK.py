from flojoy import flojoy, DataContainer, get_job_result, NodeReference


@flojoy
def FEEDBACK(default: DataContainer, referred_node: NodeReference) -> DataContainer:
    """
    The FEEDBACK node captures the result of the specified node ID. If the result is not found, it passes the result of the parent node.

    Parameters
    ----------
    referred_node : str
        The node ID to capture the result from.
    """

    result = get_job_result(referred_node.ref)
    if result:
        return result
    else:
        return default
