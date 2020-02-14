studs = (
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
    'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry',
)

plant = {
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
    'V': 'Violets',
}

class Garden(object):
    def __init__(self, diagram, students=studs):
        self.lines = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student)*2
        return [plant[p[i]] for p in self.lines for i in (index, index + 1)]