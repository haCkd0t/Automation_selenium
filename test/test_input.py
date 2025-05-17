from pages.inputs import inp
import pytest
import logging

@pytest.mark.parametrize("integer", [1])
def test_inpt(driver, integer):
    logger = logging.getLogger('selenium')
    logger.info(f"Testing input with value: {integer}")
    ob = inp(driver, integer)
    ob.inpt()

