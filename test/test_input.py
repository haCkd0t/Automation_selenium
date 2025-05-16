from pages.inputs import inp
import pytest


@pytest.mark.parametrize("integer", [1, 3, 3])
def test_inpt(driver, integer):
    ob = inp(driver, integer)
    ob.inpt()

