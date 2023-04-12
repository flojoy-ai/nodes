from flojoy import flojoy, JobResultBuilder, DataContainer

@flojoy
def IMAGE(v, params):
    data = DataContainer(type='image', r=v[0].r, g=v[0].g, b=v[0].b, a=v[0].a)
    return JobResultBuilder().from_data(data).to_plot({'plot_type':'image'})