import copy
from typing import List, Tuple

def parse_exercise_file(input_path: str) -> List[int]:
    
    with open(input_path, 'r') as file_handler:
        lines = file_handler.readlines()
        reports_list = [[int(number) for number in line.strip().split()] for line in lines]
    return reports_list

def is_report_safe(report: List[int]) -> bool:
    
    for i in range(len(report) - 1):
        if abs(report[i + 1] - report[i]) > 3 or abs(report[i + 1] - report[i]) < 1:
            return False
    
    sorted_report = sorted(report)
    inverted_sorted_report = sorted(report, reverse=True)

    if report == sorted_report or report == inverted_sorted_report:
        return True
    return False

def is_report_dampener_safe(report: List[int]) -> bool:
    if is_report_safe(report):
        return True
    else:
        for i in range(len(report)):
            new_report = copy.deepcopy(report)
            new_report.pop(i)
            if is_report_safe(new_report):
                return True
        return False
    
def count_safe_reports(reports_list: List[List[int]], safety_check_function) -> int:
    safe_reports = 0
    for report in reports_list:
        if safety_check_function(report):
            safe_reports += 1
    return safe_reports

def main(input_path):
    reports_list = parse_exercise_file(input_path)
    safe_reports = count_safe_reports(reports_list, is_report_safe)
    print("Number of safe reports: ", safe_reports)
    dampener_safe_reports = count_safe_reports(reports_list, is_report_dampener_safe)
    print("Number of dampener_safe reports: ", dampener_safe_reports)

if __name__ == "__main__":
    main("data/input_exercise2.txt")

