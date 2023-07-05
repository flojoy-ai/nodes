from flojoy import flojoy, DataContainer, get_job_result, NodeReference


@flojoy
def FEEDBACK(
    default: DataContainer, referred_node: NodeReference = NodeReference("")
) -> DataContainer:
    result = get_job_result(referred_node.ref)
    if result:
        return result
    else:
        return default
