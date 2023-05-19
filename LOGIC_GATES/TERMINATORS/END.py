from flojoy import flojoy, JobResultBuilder, DataContainer


@flojoy
def END(dc_inputs: list[DataContainer], params: dict) -> dict:
    inputs: list[DataContainer] = dc_inputs if len(dc_inputs) > 0 else []
    return JobResultBuilder().from_inputs(inputs).flow_to_nodes([]).build()
