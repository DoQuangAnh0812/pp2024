import json
import math
from domains.course import Course
from domains.student import Student

class InputManager:
    @staticmethod
    def input_students(mark_sheet):
        num_students = int(input("Enter the number of students in the class: "))
        students_data = []
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (mm/dd/yyyy): ")
            students_data.append({"id": student_id, "name": name, "dob": dob})
            mark_sheet.students.append(Student(student_id, name, dob))
        with open("students.txt", "w") as file:
            json.dump(students_data, file)

    @staticmethod
    def input_courses(mark_sheet):
        num_courses = int(input("Enter the number of courses: "))
        courses_data = []
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credit = int(input("Enter course credits: "))
            courses_data.append({"id": course_id, "name": name, "credit": credit})
            mark_sheet.courses.append(Course(course_id, name, credit))
        with open("courses.txt", "w") as file:
            json.dump(courses_data, file)

    @staticmethod
    def input_marks(mark_sheet):
        marks_data = {}
        for student in mark_sheet.students:
            marks_data[student.id] = {}
            for course in mark_sheet.courses:
                mark = float(input(f"Enter marks for {student.name} in {course.name}: "))
                mark = math.floor(mark * 10) / 10  
                marks_data[student.id][course.id] = mark
                student.add_mark(course.id, mark)
        with open("marks.txt", "w") as file:
            json.dump(marks_data, file)
