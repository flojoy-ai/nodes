from flojoy import flojoy, JobResultBuilder


@flojoy
def END(v, params):
    print('inputs passed to END: ', v)
    return JobResultBuilder()\
        .from_inputs(v)\
        .flow_to_nodes([])\
        .build()
