from flojoy import flojoy, run_in_venv, Vector


@flojoy
@run_in_venv(
    pip_dependencies=[
        "onnxruntime",
        "numpy",
        "onnx",
    ]
)
def ONNX_MODEL(
    file_path: str,
    default: Vector,
) -> Vector:
    """ONNX_MODEL loads a serialized ONNX model and uses it to make predictions using ONNX Runtime.

    On the one hand, ONNX is an open format to represent deep learning models.
    ONNX defines a common set of operators - the building blocks of machine learning
    and deep learning models - and a common file format to enable AI developers
    to use models with a variety of frameworks, tools, runtimes, and compilers.

    See: https://onnx.ai/

    On the other hand, ONNX Runtime is a high-performance inference engine for machine
    learning models in the ONNX format. ONNX Runtime has proved to considerably increase
    performance in inferencing for a broad range of ML models and hardware platforms.

    See: https://onnxruntime.ai/docs/

    See the Model Zoo for a collection of pre-trained models for common
    machine learning tasks: https://github.com/onnx/models

    Parameters
    ----------
    file_path : str
        Path to a local ONNX model to load and use for prediction.

    default : Vector
        The input tensor to use for prediction.
        For now, only a single input tensor is supported.
        Note that the input tensor shape is not checked against the model's input shape.

    Returns
    -------
    Vector:
        The predictions made by the ONNX model.
        For now, only a single output tensor is supported.
    """

    import onnx
    import numpy as np
    import onnxruntime as rt

    # Pre-loading the serialized model to validate whether is well-formed or not.
    model = onnx.load(file_path)
    onnx.checker.check_model(model)

    input_tensor = default.v

    # Using ONNX runtime for the ONNX model to make predictions.
    sess = rt.InferenceSession(file_path)

    # TODO(jjerphan): Assuming a single input and a single output for now.
    input_name = sess.get_inputs()[0].name
    label_name = sess.get_outputs()[0].name

    # TODO(jjerphan): For now NumPy is assumed to be the main backend for Flojoy.
    # We might adapt it in the future so that we can use other backends
    # for tensor libraries for application using Deep Learning libraries.
    pred_onx = sess.run(
        [label_name], {input_name: np.asarray(input_tensor, dtype=np.float32)}
    )[0]

    return Vector(v=pred_onx)
