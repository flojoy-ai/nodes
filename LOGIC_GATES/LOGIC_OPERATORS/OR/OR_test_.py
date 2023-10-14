from flojoy import Boolean


def test_OR(mock_flojoy_decorator):
    import OR

    x = Boolean(b=True)
    y = Boolean(b=False)

    return1 = OR.OR(x,y)
    return2 = OR.OR(x,x)
    return3 = OR.OR(y,y)

    assert return1.b == True
    assert return2.b == True
    assert return3.b == False