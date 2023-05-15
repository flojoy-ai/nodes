from flojoy import JobResultBuilder, flojoy


@flojoy
def GOTO(dc_inputs, params):
    goto_node_id = params.get("goto_node_id", None)
    next_nodes = [goto_node_id] if goto_node_id is not None else []

    return JobResultBuilder().from_inputs(dc_inputs).flow_to_nodes(next_nodes).build()
