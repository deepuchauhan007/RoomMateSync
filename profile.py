def get_choice(prompt, choices):
    while True:
        value = input(prompt).strip()

        if value.lower() in [choice.lower() for choice in choices]:
            for choice in choices:
                if value.lower() == choice.lower():
                    return choice

        print("Invalid choice. Please select from:", ", ".join(choices))



def create_profile(students, save_students):
    print("\n--- Create Student Profile ---")

    name = input("Enter your name: ")

    while name.strip() == "":
        print("Name cannot be empty.")
        name = input("Enter your name: ")

    student_id = input("Enter your student ID: ")

    while True:
        if student_id.strip() == "":
            print("Student ID cannot be empty.")

        elif any(student["student_id"] == student_id for student in students):
            print("This Student ID already exists.")

        else:
            break

        student_id = input("Enter your student ID: ")

    sleep_time = input("Usual sleep time: ")
    wake_time = input("Usual wake-up time: ")
    study_time = input("Preferred study time: ")

    noise = get_choice(
        "Noise preference (Low/Medium/High): ",
        ["Low", "Medium", "High"]
    )

    cleanliness = get_choice(
        "Cleanliness level (Low/Medium/High): ",
        ["Low", "Medium", "High"]
    )

    light = get_choice(
        "Light preference while sleeping (On/Off): ",
        ["On", "Off"]
    )

    fan = get_choice(
        "Fan preference (Low/Medium/High): ",
        ["Low", "Medium", "High"]
    )

    odour = get_choice(
        "Odour sensitivity (Low/Medium/High): ",
        ["Low", "Medium", "High"]
    )

    visitors = get_choice(
        "Visitor preference (Rare/Sometimes/Often): ",
        ["Rare", "Sometimes", "Often"]
    )

    profile = {
        "name": name,
        "student_id": student_id,
        "sleep_time": sleep_time,
        "wake_time": wake_time,
        "study_time": study_time,
        "noise": noise,
        "cleanliness": cleanliness,
        "light": light,
        "fan": fan,
        "odour": odour,
        "visitors": visitors
    }

    students.append(profile)
    save_students(students)

    print("\nProfile created successfully!")
    print("Student:", name)
    print("Student ID:", student_id)


def edit_profile(students, save_students):
    print("\n--- Edit Student Profile ---")

    student_id = input("Enter Student ID: ")

    selected_student = None

    for student in students:
        if student["student_id"] == student_id:
            selected_student = student
            break

    if selected_student is None:
        print("Student ID not found.")
        return

    print("\nPress Enter to keep the existing value.")

    value = input(f"Sleep time [{selected_student['sleep_time']}]: ")
    if value.strip() != "":
        selected_student["sleep_time"] = value

    value = input(f"Wake-up time [{selected_student['wake_time']}]: ")
    if value.strip() != "":
        selected_student["wake_time"] = value

    value = input(f"Study time [{selected_student['study_time']}]: ")
    if value.strip() != "":
        selected_student["study_time"] = value

    value = input(f"Noise preference [{selected_student['noise']}]: ")
    if value.strip() != "":
        selected_student["noise"] = value

    value = input(f"Cleanliness level [{selected_student['cleanliness']}]: ")
    if value.strip() != "":
        selected_student["cleanliness"] = value

    value = input(f"Light preference [{selected_student['light']}]: ")
    if value.strip() != "":
        selected_student["light"] = value

    value = input(f"Fan preference [{selected_student['fan']}]: ")
    if value.strip() != "":
        selected_student["fan"] = value

    value = input(f"Odour sensitivity [{selected_student['odour']}]: ")
    if value.strip() != "":
        selected_student["odour"] = value

    value = input(f"Visitor preference [{selected_student['visitors']}]: ")
    if value.strip() != "":
        selected_student["visitors"] = value

    save_students(students)

    print("\nProfile updated successfully!")