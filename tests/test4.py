
import sys
sys.path.append('./days/')
import pytest

from exercise4 import count_xmas_words, _get_vertical_lines, _get_diagonal_lines
MATRIX_LINES = []

@pytest.mark.parametrize("input_lines, output_lines", [
    (["ABCD", "EFGH", "IJKL"], ["AEI", "BFJ", "CGK", "DHL"]),
    (["ABC", "DEF", "GHI", "JKL"], ["ADGJ", "BEHK", "CFIL"]),

])
def test_get_vertical_lines(input_lines, output_lines):
    assert _get_vertical_lines(input_lines) == output_lines

@pytest.mark.parametrize("input_lines, output_lines", [
    (["ABCD", "EFGH", "IJKL"], ["I", "EJ", "AFK", "BGL", "CH", "D", "L", "HK", "DGJ", "CFI", "BE", "A"]),

])
def test_get_diagonal_lines(input_lines, output_lines):
    assert _get_diagonal_lines(input_lines) == output_lines

@pytest.mark.parametrize("input_lines, expected", [
    (["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"], 18)
])
def test_xmas_parsing(input_lines, expected):
    assert count_xmas_words(input_lines) == expected
