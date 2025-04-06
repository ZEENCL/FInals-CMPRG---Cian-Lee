class Schools:
    def __init__(self, name, students):
        self._name = name
        self._students = students

    def get_average_grade(self):
        total_grades = 0
        total_students = len(self._students)
        for student in self._students:
            total_grades += sum(student['grades']) / len(student['grades'])
        return total_grades / total_students
    
    def get_average_GPA(self):
        total_GPA = sum(student['gpa'] for student in self._students)
        return total_GPA / len(self._students)
    
    def get_info(self):
        for student in self._students:
            print(f"Name: {student['name']}, Grades: {student['grades']}, GPA: {student['gpa']}")