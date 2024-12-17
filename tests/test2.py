
import sys
sys.path.append('./days/')
import pytest

from exercise2 import is_report_safe, is_report_dampener_safe

@pytest.mark.parametrize("report, report_safeness", [
    ([1,2,3,4], True),
    ([5,3,2], True),
    ([5,2,3], False),
    ([7,6,4,2,1], True),
    ([1,2,7,8,9], False),
    ([9,7,6,2,1], False),
    ([1,3,2,4,5], False),
    ([8,6,4,4,1], False),
    ([1,3,6,7,9], True),
])
def test_calculate_safeness(report, report_safeness):
    assert is_report_safe(report) == report_safeness

@pytest.mark.parametrize("report, report_safeness", [
    ([7,6,4,2,1], True),
    ([1,2,7,8,9], False),
    ([9,7,6,2,1], False),
    ([1,3,2,4,5], True),
    ([8,6,4,4,1], True),
    ([1,3,6,7,9], True),
])
def test_calculate_dampener_safeness(report, report_safeness):
    assert is_report_dampener_safe(report) == report_safeness

