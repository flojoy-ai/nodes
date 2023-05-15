from flojoy import flojoy, JobResultBuilder


@flojoy
def END(dc_inputs, params):
    inputs = dc_inputs if len(dc_inputs) > 0 else []
    return JobResultBuilder().from_inputs(inputs).flow_to_nodes([]).build()
