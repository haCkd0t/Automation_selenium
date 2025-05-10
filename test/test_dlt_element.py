import pytest
from test import actions


def test_dlt_element(driver, wait):
    result = actions.Dlt_element(driver, wait)
    assert result, "Failed"
