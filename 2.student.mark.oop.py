class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class MarkSheet:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (mm/dd/yyyy): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id, name))

    def input_marks(self):
        for student in self.students:
            for course in self.courses:
                mark = float(input(f"Enter marks for {student.name} in {course.name}: "))
                self.marks[(student.id, course.id)] = mark

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        key = (student_id, course_id)
        if key in self.marks:
            print(f"Marks for student {student_id} in course {course_id} is : {self.marks[key]}")
        else:
            print("Marks not available for the given student and course.")

mark_sheet = MarkSheet()
mark_sheet.input_students()
mark_sheet.input_courses()
mark_sheet.input_marks()
mark_sheet.list_students()
mark_sheet.list_courses()
mark_sheet.show_student_marks()





