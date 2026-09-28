def find_student(students, student_id):
    for student in students:
        if student["student_id"] == student_id:
            return student

    return None


def calculate_compatibility(student1, student2):
    preferences = [
        "sleep_time",
        "wake_time",
        "study_time",
        "noise",
        "cleanliness",
        "light",
        "fan",
        "odour",
        "visitors"
    ]

    matched = 0

    for preference in preferences:
        if student1[preference].strip().lower() == student2[preference].strip().lower():
            matched += 1

    score = (matched / len(preferences)) * 100

    if score >= 80:
        level = "High"
    elif score >= 60:
        level = "Moderate"
    else:
        level = "Low"

    return matched, len(preferences) - matched, score, level


def compare_profiles(students):
    print("\n--- Compare Roommates ---")

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

    preferences = [
        "sleep_time",
        "wake_time",
        "study_time",
        "noise",
        "cleanliness",
        "light",
        "fan",
        "odour",
        "visitors"
    ]

    print("\n--- Preference Comparison ---")

    for preference in preferences:
        value1 = student1[preference]
        value2 = student2[preference]

        if value1.strip().lower() == value2.strip().lower():
            print(f"{preference.title()}: Match")
        else:
            print(f"{preference.title()}: Different")

    matched, different, score, level = calculate_compatibility(
        student1, student2
    )

    print("\n--- Compatibility Result ---")
    print("Student 1:", student1["name"])
    print("Student 2:", student2["name"])
    print("Matching preferences:", matched)
    print("Different preferences:", different)
    print(f"Compatibility Score: {score:.2f}%")
    print("Compatibility Level:", level)