from flojoy import flojoy, DataContainer, get_job_result, DefaultParams  # type:ignore


@flojoy
def FEEDBACK(
    default: DataContainer, default_parmas: DefaultParams, referred_node: str = ""
) -> DataContainer:
    result = get_job_result(referred_node)
    if result:
        return result
    else:
        return default
