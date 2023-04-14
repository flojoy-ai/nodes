from flojoy import flojoy, JobResultBuilder


@flojoy
def END(v, params):
    inputs = v if len(v) > 0 else []
    return JobResultBuilder()\
        .from_inputs(inputs)\
        .flow_to_nodes([])\
        .build()
