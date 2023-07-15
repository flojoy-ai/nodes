from flojoy import OrderedPair, Scalar, Vector


def get_param_keys(
    data_container: OrderedPair | Scalar | Vector,
) -> OrderedPair | Scalar | Vector:
    match data_container:
        case OrderedPair():
            return data_container.y
        case Scalar():
            return data_container.c
        case Vector():
            return data_container.v
