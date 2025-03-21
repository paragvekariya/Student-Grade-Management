student_grade = { }

def add_student(name, grade):
    student_grade[name] = grade
    #[sage] demo
    print(f"Added {name} with a {grade}")


    #upade a student grade

def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        # parag = 300 
        print(f"{name} with marks are upadated {grade}")


    else:
        print(f"{name} is not found!")

    # deket a student

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} is not found!")

    # view all student
    def display_all_student():
        if student_grade in student_grade.items():
            print(f"{name} : {grades}")

        else:
            print("No student found/added")


def main():
    while True:
        print('\n student grades management system')
        print("1. add student")
        print("2. update student")
        print("3.delete student")
        print("4. view student")
        print("5. Exit") 


        choice = int (input("Enter your choice ="))
        if choice == 1:
            name = input ("Enter student name =")
            grade = int(input("enter student grade ="))
            add_student(name, grade)

        elif choice ==2:
            name = input("enter student name = ")
            grade = int(input("enter student grade ="))
            add_student(name, grade)

        elif choice == 3:
            name = input("enter student name = ")
            delete_student(name)

        elif choice == 4:
            display_all_student()

        elif choice == 5:
            print("closing the programm...")
            break

        else:
            print("invalid choice")
    

        
