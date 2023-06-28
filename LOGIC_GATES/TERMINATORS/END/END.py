from flojoy import flojoy, JobResultBuilder, DataContainer


# TODO: Implement arbitrary number of inputs
@flojoy(node_type="TERMINATOR")
def END(default: DataContainer) -> dict:
    return JobResultBuilder().from_inputs([default]).flow_to_nodes([]).build()
