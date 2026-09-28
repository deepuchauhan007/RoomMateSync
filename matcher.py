from compatibility import find_student, calculate_compatibility


def find_best_match(students):
    print("\n--- Find Best Match ---")

    if len(students) < 2:
        print("At least two student profiles are required.")
        return

    student_id = input("Enter Student ID: ")

    student = find_student(students, student_id)

    if student is None:
        print("Student ID not found.")
        return

    best_match = None
    best_score = -1

    for other_student in students:

        if other_student["student_id"] == student_id:
            continue

        matched, different, score, level = calculate_compatibility(
            student,
            other_student
        )

        if score > best_score:
            best_score = score
            best_match = other_student
            best_details = (matched, different, level)

    matched, different, level = best_details

    print("\n--- Best Match Result ---")
    print("Student:", student["name"])
    print("Best Match:", best_match["name"])
    print("Matching preferences:", matched)
    print("Different preferences:", different)
    print(f"Compatibility Score: {best_score:.2f}%")
    print("Compatibility Level:", level)