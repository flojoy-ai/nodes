from flojoy import OrderedPair, Scalar, Vector


def get_val(
    data_container: OrderedPair | Scalar | Vector,
) -> OrderedPair | Scalar | Vector:
    if isinstance(data_container, OrderedPair):
        return data_container.y
    elif isinstance(data_container, Scalar):
        return data_container.c
    elif isinstance(data_container, Vector):
        return data_container.v
