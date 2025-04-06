from .schools import Schools

class SchoolTwo(Schools):
    def __init__(self, students):
        super().__init__("School Two", students)

    def get_grades(self):
        print(f"Grades for {self._name}:\n")
        self.get_info()
        print()
        print(f"Average Grade: {round(self.get_average_grade(), 2)}")
        print(f"Average GPA: {round(self.get_average_GPA(), 2)}")