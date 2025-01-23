import re
from typing import Tuple


def get_list_of_operations(input_string: str) -> list[Tuple[str, str]]:
    pattern = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.findall(pattern, input_string)
    return matches

def calculate_valid_substring(input_string):
    sub_strings = input_string.split("don't()")
    valid_strings = sub_strings[0]
    for sub_string in sub_strings[1:]:
        sub_strings = sub_string.split("do()")
        if len(sub_strings) > 1:
            valid_strings += "".join(sub_strings[1:])
    return valid_strings

def calculate_value_from_matches(matches):
    count = 0
    for match in matches:
        count += int(match[0]) * int(match[1])
    return count

def extract_memory_operations_value(input_string):
    matches = get_list_of_operations(input_string)
    return calculate_value_from_matches(matches)

def extract_conditioned_memory_operations_value(input_string):
    valid_substring = calculate_valid_substring(input_string)
    matches = get_list_of_operations(valid_substring)
    return calculate_value_from_matches(matches)

def main(input_path):
    with open(input_path, "r") as file:
        input_string = file.read()
        print(extract_memory_operations_value(input_string))
        print(extract_conditioned_memory_operations_value(input_string))

if __name__ == "__main__":
    main("data/input_exercise3.txt")

