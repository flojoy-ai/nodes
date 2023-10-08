from flojoy import Boolean, Scalar, Vector
import numpy as np

def test_COMPOUND_ARITHMETIC(mock_flojoy_decorator):
    import COMPOUND_ARITHMETIC

    x = Boolean(b=True)
    y = Boolean(b=False)

    # return1 = COMPOUND_ARITHMETIC.COMPOUND_ARITHMETIC(Vector(v=[1,2,3]),Vector(v=[1,2,3]), "MULTIPLY")
    # return2 = COMPOUND_ARITHMETIC.IMPLIES(x,x)
    # return3 = IMPLIES.IMPLIES(y,y)
    x = Vector(v=np.arange(-10, 10, 1))
    y = Vector(v=np.arange(-20, 20, 2))
    res = COMPOUND_ARITHMETIC.COMPOUND_ARITHMETIC(Vector(v=[1,2,3]),Vector(v=[1,2,3]), "ADD")
    print(res.v)
    assert np.array_equal(res.v, [2,4,6])

    # assert return1.c == 8
    # assert return2.b == True
    # assert return3.b == True