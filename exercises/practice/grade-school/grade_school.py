class School:
    def __init__(self):
        self.students = {} # maps student name -> grade
        self._add_record = []

    def add_student(self, name, grade):
        if name not in self.students:
            self.students[name] = grade
            self._add_record.append(True)
        else:
            self._add_record.append(False)

    def roster(self):
        sorted_roster = sorted(self.students.items(), key=lambda item: (item[1], item[0]))
        return [name for name, _ in sorted_roster]

    def grade(self, grade_number):
        return sorted([name for name, grade in self.students.items() if grade == grade_number])

    def added(self):
        return self._add_record
