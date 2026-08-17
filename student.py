from typing import Dict, List, Tuple, Union


# Define a type alias for clarity
StudentData = Dict[str, float]


def calculate_average(marks: List[float]) -> float:
    """
    Calculates the arithmetic mean of a list of marks.
    """
    if not marks:
        return 0.0

    return sum(marks) / len(marks)


def find_highest_and_lowest(marks: List[float]) -> Tuple[float, float]:
    """
    Finds the maximum and minimum marks from a list.
    """
    if not marks:
        return 0.0, 0.0

    return max(marks), min(marks)


def get_grade(mark: float) -> str:
    """
    Determines the letter grade for a given numerical mark.
    """
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


def process_student_records(
    students: StudentData
) -> Dict[str, Union[float, Dict[str, str]]]:
    """
    Processes student data and calculates class statistics
    and individual grades.
    """

    if not students:
        return {
            "average": 0.0,
            "highest": 0.0,
            "lowest": 0.0,
            "grades": {}
        }

    marks = list(students.values())

    # Calculate statistics
    average = calculate_average(marks)
    highest, lowest = find_highest_and_lowest(marks)

    # Assign grades to each student
    individual_grades = {
        name: get_grade(mark)
        for name, mark in students.items()
    }

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grades": individual_grades
    }


def display_report(students: StudentData, report: Dict) -> None:
    """
    Prints a formatted performance report.
    """

    print("=" * 45)
    print(f"{'STUDENT NAME':<15} | {'MARK':<8} | {'GRADE':<5}")
    print("=" * 45)

    for name, mark in students.items():
        grade = report["grades"][name]
        print(f"{name:<15} | {mark:<8.1f} | {grade:<5}")

    print("=" * 45)
    print(f"Class Average : {report['average']:.2f}")
    print(f"Highest Mark  : {report['highest']:.1f}")
    print(f"Lowest Mark   : {report['lowest']:.1f}")
    print("=" * 45)


def main():
    # Sample student dataset
    student_marks: StudentData = {
        "Alice": 85.5,
        "Bob": 92.0,
        "Charlie": 58.0,
        "Diana": 74.5,
        "Ethan": 45.0,
        "Fiona": 89.0
    }

    # Process the data
    report = process_student_records(student_marks)

    # Display the results
    display_report(student_marks, report)


if __name__ == "__main__":
    main()
