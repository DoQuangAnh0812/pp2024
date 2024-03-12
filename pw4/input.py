import math 

from domains.student import Student
from domains.course import Course

class InputManager:
    @staticmethod
    def input_students(mark_sheet):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (mm/dd/yyyy): ")
            mark_sheet.students.append(Student(student_id, name, dob))

    @staticmethod
    def input_courses(mark_sheet):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credit = int(input("Enter course credits: "))
            mark_sheet.courses.append(Course(course_id, name, credit))

    @staticmethod
    def input_marks(mark_sheet):
        for student in mark_sheet.students:
            for course in mark_sheet.courses:
                mark = float(input(f"Enter marks for {student.name} in {course.name}: "))
                mark = math.floor(mark * 10) / 10  
                student.add_mark(course.id, mark)
