
import pytest
from triangulation import calculate as calc

@pytest.fixture(scope='function')
def setup():
    return 3

def test_fail(setup):
    assert setup == 2

def test_calculate():
    assert calc.check_intersection()

def test_calculate_2():
    assert calc.check_orientation()
