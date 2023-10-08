from flojoy import flojoy, Boolean, OrderedPair, Scalar, Vector
from typing import Literal
import sys 
# sys.path.insert(0, '../../TRANSFORMERS/ARITHMETIC/MULTIPLY')
# sys.path.insert(0, 'PYTHON/nodes/TRANSFORMERS/ARITHMETIC/MULTIPLY')
# sys.path.insert(0, 'PYTHON/nodes/TRANSFORMERS/ARITHMETIC/MULTIPLY')
# from ADD import ADD
# from MULTIPLY import MULTIPLY
from nodes.TRANSFORMERS.ARITHMETIC.MULTIPLY import MULTIPLY

@flojoy
def COMPOUND_ARITHMETIC(x: Boolean | OrderedPair | Scalar | Vector, y: Boolean | OrderedPair | Scalar | Vector,
                        operation: Literal['ADD', 'MULTIPLY', 'AND', 'OR', 'XOR']) -> Boolean:
    if operation == "ADD":
        pass
    elif operation == "MULTIPLY":
        return MULTIPLY(x,y)
    elif operation == "AND":
        pass
    elif operation == "OR":
        pass
    elif operation == "XOR":
        pass