from storage import load_students, save_students
from profile import create_profile, edit_profile
from compatibility import compare_profiles
from conflict_detector import detect_conflicts
from matcher import find_best_match
from report import generate_report


students = load_students()


def show_menu():
    print("\n==============================")
    print("        ROOMMATESYNC")
    print("==============================")
    print("1. Create Student Profile")
    print("2. Compare Roommates")
    print("3. Find Best Match")
    print("4. Detect Conflicts")
    print("5. View Report")
    print("6. Edit Student Profile")
    print("7. Exit")
    print("==============================")




def view_profile():
    if len(students) == 0:
            print("\nNo student profile found.")
            return

    print("\n========== STUDENT PROFILE ==========")

    for student in students:
        print("Name              :", student["name"])
        print("Student ID        :", student["student_id"])
        print("Sleep Time        :", student["sleep_time"])
        print("Wake-up Time      :", student["wake_time"])
        print("Study Time        :", student["study_time"])
        print("Noise Preference  :", student["noise"])
        print("Cleanliness       :", student["cleanliness"])
        print("Light Preference  :", student["light"])
        print("Fan Preference    :", student["fan"])
        print("Odour Sensitivity :", student["odour"])
        print("Visitor Preference:", student["visitors"])
        print("====================================")



def main():
    print("Welcome to RoomMateSync!")
    print("A simple roommate preference matching system.")

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            create_profile(students, save_students)

        elif choice == "2":
            compare_profiles(students)

        elif choice == "3":
            find_best_match(students)

        elif choice == "4":
            detect_conflicts(students)

        elif choice == "5":
            generate_report(students)

        elif choice == "6":
            edit_profile(students, save_students)

        elif choice == "7":
            print("\nThank you for using RoomMateSync!")
            break

        else:
            print("\nInvalid choice. Please try again.")

     
if __name__ == "__main__":
    main()