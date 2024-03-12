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
        total_weighted_sum = 0
        total_credits = 0
        
        for course in courses:
            if course.id in self.marks:
                mark = self.marks[course.id]
                total_weighted_sum += mark * course.credit
                total_credits += course.credit
        
        if total_credits == 0:
            return 0
        return total_weighted_sum / total_credits
