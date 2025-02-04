import re
import copy as cp

def _get_vertical_lines(lines = list()) -> list:
    vertical_lines = list()
    for i in range(len(lines)):
        vertical_line = ""
        for j in range(len(lines)):
            vertical_line += lines[j][i]
        vertical_lines.append(vertical_line)
    return vertical_lines

def _get_diagonal_lines(lines = list()) -> list:
    diagonal_lines = list()
    for i in range(len(lines)):
        diagonal_line = ""
        for j in range(len(lines)):
            diagonal_line += lines[j][j]
        diagonal_lines.append(diagonal_line)
    return diagonal_lines


def count_xmas_words(lines = list(), word: str = "XMAS") -> int:
    whole_lines = cp.copy(lines)
    whole_lines += _get_vertical_lines(lines)
    whole_lines += _get_diagonal_lines(lines)

    count = 0
    for line in whole_lines:
        count += len(re.findall(word, line))
        count += len(re.findall(word[::-1], line))
    return count

def main(input_path):
    with open(input_path, "r") as file:
        input_lines = file.readlines()
        print(count_xmas_words(input_lines))
        

if __name__ == "__main__":
    main("data/input_exercise4.txt")

