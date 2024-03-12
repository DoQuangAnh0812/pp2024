class OutputManager:
    @staticmethod
    def list_students(mark_sheet):
        print("\nList of Students:")
        for student in mark_sheet.students:
            print(student)

    @staticmethod
    def list_courses(mark_sheet):
        print("\nList of Courses:")
        for course in mark_sheet.courses:
            print(course)

    @staticmethod
    def show_student_marks(mark_sheet):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        for student in mark_sheet.students:
            if student.id == student_id:
                if course_id in student.marks:
                    print(f"Marks for student {student_id} in course {course_id} is : {student.marks[course_id]}")
                else:
                    print("Marks not available for the given student and course.")
                return
        print("Student not found.")

    @staticmethod
    def sort_students_by_gpa(mark_sheet):
        mark_sheet.students.sort(key=lambda student: student.calculate_gpa(mark_sheet.courses), reverse=True)
        print("\nStudents sorted by GPA:")
        for student in mark_sheet.students:
            print(student)
