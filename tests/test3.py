
import sys
sys.path.append('./days/')
import pytest

from exercise3 import extract_memory_operations_value, extract_conditioned_memory_operations_value

@pytest.mark.parametrize("input_string, expected_output", [
    ("mul(2,3)", 6),
    ("mul(3,-3)", -9),
    ("mul(-3,-3)", 9),
    ("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", 161)
])
def test_extract_memory_operations_value(input_string, expected_output):
    assert extract_memory_operations_value(input_string) == expected_output


@pytest.mark.parametrize("input_string, expected_output", [
    ("mul(2,3)", 6),
    ("mul(3,-3)", -9),
    ("mul(-3,-3)", 9),
    ("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", 161),
    ("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", 48)
])
def test_extract_conditioned_memory_operations_value(input_string, expected_output):
    assert extract_conditioned_memory_operations_value(input_string) == expected_output

