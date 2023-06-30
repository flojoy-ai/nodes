from flojoy import flojoy, JobResultBuilder, DataContainer, DefaultParams

@flojoy(node_type='TERMINATOR')
def END(default: DataContainer) -> dict:
    return JobResultBuilder().from_inputs([default]).flow_to_nodes([]).build()