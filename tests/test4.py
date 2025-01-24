
import sys
sys.path.append('./days/')
import pytest

from exercise4 import count_xmas_words

@pytest.mark.parametrize("input_lines, expected", [
    (["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"], 18)
])
def test_xmas_parsing(input_lines, expected):
    assert count_xmas_words(input_lines) == expected
