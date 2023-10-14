from flojoy import Boolean


def test_NOT_OR(mock_flojoy_decorator):
    import NOT_OR

    x = Boolean(b=True)
    y = Boolean(b=False)

    return1 = NOT_OR.NOT_OR(x,y)
    return2 = NOT_OR.NOT_OR(x,x)
    return3 = NOT_OR.NOT_OR(y,y)

    assert return1.b == False
    assert return2.b == False
    assert return3.b == True