students = []


def add_student(name: str) -> None:
    """
    Adds a student to the list of students.

    :param name: str
        The name of the student.

    :return: None
    """
    try:
        if not name.isalpha():
            raise ValueError
        students.append({'name': name, 'grades': []})

    except ValueError:
        print('Invalid student name.')


def add_grades(name: str) -> None:
    """
    Adds grades to the list of grades of the chosen student.

    :param name: str
        The name of the student.

    :return: None
    """

    if not len(students):
        print("No students were found.")
        return

    try:
        found = False

        for student in students:
            if student['name'] == name:
                found = True

                while True:
                    try:
                        grade_input = input("Enter a grade (or 'done' to finish): ")

                        if grade_input.lower() == 'done':
                            return

                        if int(grade_input) > 100 or int(grade_input) < 0:
                            raise ValueError

                        student['grades'].append(int(grade_input))

                    except ValueError:
                        print("Grade was invalid. Please enter a number between 0 and 100.")

        if not found:
            raise KeyError

    except KeyError:
        print(f"Student {name} was not found.")


def full_report() -> None:
    """
    Prints the full report of all students.

    :return: None
    """

    print("--- Student report ---")
    avg_grades = []

    if not len(students):
        print("No students were found.")
        return

    for student in students:
        try:
            avg_grade = sum(student['grades'])/len(student['grades'])
            avg_grades.append(avg_grade)

            print(f"{student['name']}'s average grade is {avg_grade}")

        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A.")

    if not len(avg_grades):
        print("None of the students have any grades.")
        return

    print(f"Max Average: {max(avg_grades)}"
          f"\nMin Average: {min(avg_grades)}"
          f"\nOverall Average: {sum(avg_grades)/len(avg_grades)}")


def top_student() -> None:
    """
    Finds the top student in the list of students.

    :return: None
    """
    if not len(students):
        print("No students were found.")
        return

    try:
        best = max(students, key = lambda s: sum(s["grades"]) / len(s["grades"]) if s["grades"] else 0)
        avg = sum(best["grades"]) / len(best["grades"])

        print(f"The student with the highest average is {best['name']} with a grade of {avg}")

    except ZeroDivisionError:
        print("None of the students have any grades.")


def main() -> None:
    """
    Main function of the program.

    :return: None
    """
    print("--- Student Grade Analyzer ---")

    while True:
        try:
            print("1. Add a new student"
                  "\n2. Add grades for a student"
                  "\n3. Generate a full report"
                  "\n4. Find the top student"
                  "\n5. Exit program")

            choice = int(input("Enter your choice: "))

            if choice > 5 or choice < 1:
                raise ValueError

            match choice:
                case 1:
                    add_student(input("Enter student name: ").capitalize())

                case 2:
                    add_grades(input("Enter student name: ").capitalize())

                case 3:
                    full_report()

                case 4:
                    top_student()

                case 5:
                    break

        except ValueError:
            print("Your choice was invalid. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()