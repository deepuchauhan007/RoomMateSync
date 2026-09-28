from compatibility import find_student, calculate_compatibility


def generate_report(students):
    print("\n--- Match Report ---")

    if len(students) < 2:
        print("At least two student profiles are required.")
        return

    student_id1 = input("Enter first Student ID: ")
    student_id2 = input("Enter second Student ID: ")

    student1 = find_student(students, student_id1)
    student2 = find_student(students, student_id2)

    if student1 is None or student2 is None:
        print("One or both Student IDs were not found.")
        return

    if student_id1 == student_id2:
        print("Please enter two different Student IDs.")
        return

    matched, different, score, level = calculate_compatibility(
        student1, student2
    )

    print("\n==============================")
    print("        MATCH REPORT")
    print("==============================")
    print("Student 1:", student1["name"])
    print("Student 2:", student2["name"])
    print("------------------------------")
    print("Matching preferences:", matched)
    print("Different preferences:", different)
    print(f"Compatibility Score: {score:.2f}%")
    print("Compatibility Level:", level)
    print("==============================")