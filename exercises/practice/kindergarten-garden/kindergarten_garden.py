PLANTS = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets",
}

DEFAULT_STUDENTS = [
    "Alice", "Bob", "Charlie", "David", 
    "Eve", "Fred", "Ginny", "Harriet", 
    "Ileana", "Joseph", "Kincaid", "Larry",
]

class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        diagram_rows = [
            [line[i:i+2] for i in range(0, len(line), 2)]
            for line in diagram.splitlines()
        ]
        self._diagram_cols = list(zip(*diagram_rows))
        self._students_idx = {
            name: idx for idx, name in enumerate(sorted(students))
        }

    def plants(self, name):
        idx = self._students_idx[name]
        return [
            PLANTS[plant] 
            for row in self._diagram_cols[idx]
            for plant in row
        ]
