def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    students = [
        {
            "id": input("Enter student ID: "),
            "name": input("Enter student name: "),
            "dob": input("Enter student Date of Birth (mm/dd/yyyy): "),
        }
        for _ in range(num_students)
    ]
    return students

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = [
        {"id": input("Enter course ID: "), "name": input("Enter course name: ")}
        for _ in range(num_courses)
    ]
    return courses

def input_marks(students, courses):
    marks = {
        (student['id'], course['id']): float(input(f"Enter marks for {student['name']} in {course['name']}: "))
        for student in students
        for course in courses
    }
    return marks

def list_students(students):
    print("\nList of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def list_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def show_student_marks(students, courses, marks):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    key = (student_id, course_id)
    if key in marks:
        print(f"Marks for student {student_id} in course {course_id} is : {marks[key]}")
    else:
        print("Marks not found for the given student and course.")


students = input_students()
courses = input_courses()
marks = input_marks(students, courses)
list_students(students)
list_courses(courses)
show_student_marks(students, courses, marks)
