from flojoy import Boolean, Scalar


def test_COMPOUND_ARITHMETIC(mock_flojoy_decorator):
    import COMPOUND_ARITHMETIC

    x = Boolean(b=True)
    y = Boolean(b=False)

    return1 = COMPOUND_ARITHMETIC.COMPOUND_ARITHMETIC(Scalar(c=4),Scalar(c=2), "MULTIPLY")
    # return2 = COMPOUND_ARITHMETIC.IMPLIES(x,x)
    # return3 = IMPLIES.IMPLIES(y,y)

    assert return1.c == 8
    # assert return2.b == True
    # assert return3.b == True