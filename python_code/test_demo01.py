# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
def add(x, y):
    return x + y


def test_add():
    assert add(1, 10) == 11
    assert add(1, 1) == 2
    assert add(1, 99) == 100
