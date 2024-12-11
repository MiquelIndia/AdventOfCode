from typing import List

def calculate_distance_id(list1: List, list2: List) -> int:
    list1.sort()
    list2.sort()
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
    return distance

def calculate_lists_similarity_score(list1: List, list2: List) -> int:
    list1.sort()
    list2.sort()
    similarity_score = 0
    for index1 in range(len(list1)):
        searched_number = list1[index1]
        repetitions = 0
        for index2 in range(len(list2)):
            if list2[index2] == searched_number:
                repetitions += 1
            elif list2[index2]>searched_number:                
                break
        similarity_score += repetitions*searched_number
    return similarity_score

def parse_exercise_file(input_path):
    list1 = []
    list2 = []
    with open(input_path, 'r') as file_handler:
        for line in file_handler:
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))

    return list1, list2

def main(input_path):
    list1, list2 = parse_exercise_file(input_path)
    lists_distance = calculate_distance_id(list1, list2)
    similarity_distance = calculate_lists_similarity_score(list1, list2)
    print("The lists distance is: ", lists_distance)
    print("The lists similarity score is: ", similarity_distance)

if __name__ == "__main__":
    main("data/input_exercise1.txt")

