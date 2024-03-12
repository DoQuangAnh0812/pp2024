import os
from input import InputManager
from output import OutputManager
from domains.student import Student
from domains.course import Course
from compression import compress_data, decompress_data, check_data_file

if check_data_file():
    decompress_data()

class MarkSheet:
    def __init__(self):
        self.students = []
        self.courses = []

    def calculate_average_gpa(self, student_id):
        for student in self.students:
            if student.id == student_id:
                gpa = student.calculate_gpa(self.courses)
                return gpa
        return None

mark_sheet = MarkSheet()
InputManager.input_students(mark_sheet)
InputManager.input_courses(mark_sheet)
InputManager.input_marks(mark_sheet)

OutputManager.list_students(mark_sheet)
OutputManager.list_courses(mark_sheet)
OutputManager.show_student_marks(mark_sheet)

student_id = input("Enter student ID to calculate average GPA: ")
average_gpa = mark_sheet.calculate_average_gpa(student_id)
if average_gpa is not None:
    print(f"Average GPA for student {student_id}: {average_gpa}")
else:
    print("Student not found.")

OutputManager.sort_students_by_gpa(mark_sheet)

compression_method = input("Select compression method (zip/tar): ")
if compression_method == "zip":
    compress_data()
    print("Data compressed successfully.")
elif compression_method == "tar":
    pass
else:
    print("Invalid compression method selected.")
