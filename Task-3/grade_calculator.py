# Task 3 - Program 2: Student Grade Calculator (Menu-Driven)
# Calculates student grades across 5 subjects and remembers the last entered record.


def calculate_grade(average):
    """
    Returns letter grade based on average marks:
    - 90 and above: A
    - 75 to 89: B
    - 60 to 74: C
    - 40 to 59: D
    - below 40: F
    """
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def grade_calculator_app():
    """
    Runs the menu-driven grade calculator.
    Keeps track of the most recently entered student record.
    """
    last_student = None  # Stored outside the loop to persist across menu selections

    print("\n========================================")
    print("       STUDENT GRADE CALCULATOR         ")
    print("========================================")

    while True:
        print("------------- GRADE MENU -------------")
        print("1. Enter marks for a new student")
        print("2. View grade of last entered student")
        print("3. Exit")
        print("--------------------------------------")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            if not name:
                name = "Unnamed Student"

            print("Enter marks for 5 subjects (0 to 100):")
            marks = []
            for i in range(1, 6):
                while True:
                    try:
                        score = float(input(f"  Subject {i} mark: "))
                        if 0 <= score <= 100:
                            marks.append(score)
                            break
                        else:
                            print("  >> Marks must be between 0 and 100.")
                    except ValueError:
                        print("  >> Invalid input! Please enter a valid numerical mark.")

            total = sum(marks)
            avg = total / len(marks)
            grade = calculate_grade(avg)

            last_student = {
                "name": name,
                "marks": marks,
                "total": total,
                "average": avg,
                "grade": grade
            }

            print("\n>> Student record saved successfully!")
            print(f">> Name: {name} | Average: {avg:.2f} | Grade: {grade}\n")

        elif choice == "2":
            if last_student is None:
                print("\n>> No student record found yet. Please choose option 1 to enter marks first.\n")
            else:
                print("\n------------- LAST STUDENT REPORT -------------")
                print(f"Name   : {last_student['name']}")
                print(f"Marks  : {', '.join(str(m) for m in last_student['marks'])}")
                print(f"Total  : {last_student['total']:.2f} / 500")
                print(f"Average: {last_student['average']:.2f}%")
                print(f"Grade  : {last_student['grade']}")
                print("-----------------------------------------------\n")

        elif choice == "3":
            print(">> Exiting Grade Calculator. Goodbye!\n")
            break

        else:
            print(">> Error: Invalid selection! Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    grade_calculator_app()
