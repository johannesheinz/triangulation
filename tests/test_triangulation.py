
import pytest
# import triangulation

@pytest.fixture(scope='function')
def setup():
    return 3

def test_fail(setup):
    assert setup == 2
