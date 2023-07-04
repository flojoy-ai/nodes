from flojoy import DataContainer, JobResultBuilder, flojoy, NodeReference


@flojoy
def GOTO(default: DataContainer, goto_node_id: NodeReference = NodeReference("")):
    next_nodes = [goto_node_id.ref] if goto_node_id.ref != "" else []
    return JobResultBuilder().from_inputs([default]).flow_to_nodes(next_nodes).build()
