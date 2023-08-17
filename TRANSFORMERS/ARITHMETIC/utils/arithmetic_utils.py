from flojoy import OrderedPair, Scalar, Vector, DCNpArrayType


def get_val(
    data_container: OrderedPair | Scalar | Vector,
) -> DCNpArrayType:
    if isinstance(data_container, OrderedPair):
        return data_container.y
    elif isinstance(data_container, Scalar):
        return data_container.c
    elif isinstance(data_container, Vector):
        return data_container.v

