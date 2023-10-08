from flojoy import flojoy, Boolean, OrderedPair, Scalar, Vector
from typing import Literal
from PYTHON.nodes.TRANSFORMERS.ARITHMETIC.MULTIPLY import MULTIPLY
from PYTHON.nodes.TRANSFORMERS.ARITHMETIC.ADD import ADD
from PYTHON.nodes.LOGIC_GATES.AND import AND
from PYTHON.nodes.LOGIC_GATES.OR import OR
from PYTHON.nodes.LOGIC_GATES.EXCLUSIVE_OR import EXCLUSIVE_OR

@flojoy
def COMPOUND_ARITHMETIC(x: Boolean | OrderedPair | Scalar | Vector, y: Boolean | OrderedPair | Scalar | Vector,
                        operation: Literal['ADD', 'MULTIPLY', 'AND', 'OR', 'XOR']) -> Boolean | OrderedPair | Scalar | Vector:
    if operation == "ADD":
        return ADD.ADD(x,[y])
    elif operation == "MULTIPLY":
        return MULTIPLY.MULTIPLY(x,[y])
    elif operation == "AND":
        return AND.AND(x,y)
    elif operation == "OR":
        return OR.OR(x,y)
    elif operation == "XOR":
        return EXCLUSIVE_OR.EXCLUSIVE_OR(x,y)