from flojoy import flojoy, DataContainer

@flojoy
def SELECT_ARRAY(v, params):
    '''
    Node to convert an input array with multiple columns to the selected ordered pair.

    For example, the SERIAL node can output x=time, y1=temperature, y2=pressure.
    This node will select one of temperautre and pressure columns to output.
    '''
    print('parameters passed to SELECT_ARRAY: ', params)
    COL = int(params.get('column', 0)) # Index of the selected column.

    x = v[0].x
    y = v[0].y[:, int(COL)]

    print('')
    print(x)
    print(type(x))
    print(y)
    print(type(y))
    print('')

    return DataContainer(x=x, y=y)


# @flojoy
# def Serial_MOCK (dc,params):

#     print('Running mock version of SELECT_ARRAY')

#     x = np.linspace(0, 100, 100)
#     y = np.linspace(0, 100, 100)

#     return DataContainer(x=x, y=y)
