import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def calculate_gpa(self, courses):
        total_credits = 0
        weighted_sum = 0
        for course in courses:
            if course.id in self.marks:
                mark = self.marks[course.id]
                weighted_sum += mark * course.credit
                total_credits += course.credit
        if total_credits == 0:
            return 0
        return weighted_sum / total_credits

class Course:
    def __init__(self, course_id, name, credit):
        self.id = course_id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Credits: {self.credit}"

class MarkSheet:
    def __init__(self):
        self.students = []
        self.courses = []

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
            credit = int(input("Enter course credits: "))
            self.courses.append(Course(course_id, name, credit))

    def input_marks(self):
        for student in self.students:
            for course in self.courses:
                mark = float(input(f"Enter marks for {student.name} in {course.name}: "))
                mark = math.floor(mark * 10) / 10  
                student.add_mark(course.id, mark)

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
        for student in self.students:
            if student.id == student_id:
                if course_id in student.marks:
                    print(f"Marks for student {student_id} in course {course_id} is : {student.marks[course_id]}")
                else:
                    print("Marks not found for the given student and course.")
                return
        print("Student not found.")

    def calculate_average_gpa(self, student_id):
        for student in self.students:
            if student.id == student_id:
                gpa = student.calculate_gpa(self.courses)
                return gpa
        return None

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: x.calculate_gpa(self.courses), reverse=True)

    
mark_sheet = MarkSheet()
mark_sheet.input_students()
mark_sheet.input_courses()
mark_sheet.input_marks()


student_id = input("Enter student ID to calculate average GPA: ")
average_gpa = mark_sheet.calculate_average_gpa(student_id)
if average_gpa is not None:
    print(f"Average GPA for student {student_id}: {average_gpa}")
else:
    print("Student not found.")


mark_sheet.sort_students_by_gpa()
print("\nStudents sorted by GPA:")
mark_sheet.list_students()
