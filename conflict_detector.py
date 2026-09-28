from compatibility import find_student


def detect_conflicts(students):
    print("\n--- Conflict Detector ---")

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

    conflict_fields = [
        "sleep_time",
        "study_time",
        "noise",
        "cleanliness",
        "light",
        "fan"
    ]

    conflicts = []

    print("\n--- Preference Conflicts ---")

    for field in conflict_fields:
        value1 = student1[field]
        value2 = student2[field]

        if value1.strip().lower() != value2.strip().lower():
            conflicts.append(field)

            print(f"\n{field.title()}")
            print(f"{student1['name']}: {value1}")
            print(f"{student2['name']}: {value2}")

    if len(conflicts) == 0:
        print("\nNo major preference conflicts found.")
    else:
        print(f"\nTotal conflicts: {len(conflicts)}")