import pytest


@pytest.mark.parametrize("element, suma", [(5, 10), (2, 4)])
def test_adding(element, suma):
    assert element + element == suma, f'{element} + {element} != {suma}'
