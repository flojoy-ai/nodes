from flojoy import flojoy, JobResultBuilder

@flojoy
def SCATTER(v, params):
    return JobResultBuilder().from_inputs(v).to_plot(plot_type='scatter')