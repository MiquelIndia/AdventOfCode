import re



def get_list_of_operations(input_string):
    pattern = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.findall(pattern, input_string)
    return matches


def extract_memory_operations_value(input_string):
    matches = get_list_of_operations(input_string)
    count = 0
    for match in matches:
        count += int(match[0]) * int(match[1])
    return count

def main(input_path):
    with open(input_path, "r") as file:
        input_string = file.read()
        print(extract_memory_operations_value(input_string))

if __name__ == "__main__":
    main("data/input_exercise3.txt")

