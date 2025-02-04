import re
import copy as cp

def _get_vertical_lines(lines = list()) -> list:
    vertical_lines = list()
    max_length = max(len(line) for line in lines)
    for i in range(max_length):
        vertical_line = ""
        for j in range(len(lines)):
            if i < len(lines[j]):
                vertical_line += lines[j][i]
            else:
                vertical_line += " "
        vertical_lines.append(vertical_line)
    return vertical_lines

def _get_diagonal_lines(lines = list()) -> list:
    diagonal_lines = list()
    max_length = max(len(line) for line in lines)
    
    # Get diagonals from top-left to bottom-right
    for d in range(-len(lines) + 1, max_length):
        diagonal_line = ""
        for i in range(len(lines)):
            j = i + d
            if 0 <= j < len(lines[i]):
                diagonal_line += lines[i][j]
        if diagonal_line:
            diagonal_lines.append(diagonal_line)
    
    # Get diagonals from top-right to bottom-left
    for d in range(-len(lines) + 1, max_length):
        diagonal_line = ""
        for i in range(len(lines)):
            j = len(lines[i]) - 1 - i - d
            if 0 <= j < len(lines[i]):
                diagonal_line += lines[i][j]
        if diagonal_line:
            diagonal_lines.append(diagonal_line)
    
    return diagonal_lines


def count_xmas_words(lines = list(), word: str = "XMAS") -> int:
    whole_lines = cp.copy([line.strip() for line in lines])
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

