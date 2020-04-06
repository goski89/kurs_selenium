import pytest


def test_method():
    a = 5
    b = 2
    assert a+b == 7, "a+b nie jest równe 7!"
    assert a-b == 3, "a-b nie jest równe 3!"


@pytest.mark.xfail
def test_method2():
    a = 5
    b = 2
    assert a+b == 7, "a+b nie jest równe 7!"
    assert a-b == 3, "a-b nie jest równe 3!"


def random_name():
    a = 5
    b = 2
    assert a+b == 7, "a+b nie jest równe 7!"
    assert a-b == 3, "a-b nie jest równe 3!"


def random_name_test():
    a = 5
    b = 2
    assert a+b == 7, "a+b nie jest równe 7!"
    assert a-b == 3, "a-b nie jest równe 3!"