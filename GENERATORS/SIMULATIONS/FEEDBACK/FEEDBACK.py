from flojoy import flojoy, DataContainer, get_job_result, ParameterTypes


@flojoy
def FEEDBACK(
    default: DataContainer, referred_node: ParameterTypes.NODE_REFERENCE = ""
) -> DataContainer:
    result = get_job_result(referred_node)
    if result:
        return result
    else:
        return default
