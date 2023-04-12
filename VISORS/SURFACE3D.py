from flojoy import flojoy, JobResultBuilder

@flojoy
def SURFACE3D(v, params):
    return JobResultBuilder().from_inputs(v).to_plot({'plot_type':'surface3d'})