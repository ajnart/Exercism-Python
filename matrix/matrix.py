class Matrix():
    def __init__(self, matrix_string):
        self.rows = [[int(item) for item in row.split(' ')] for row in matrix_string.split('\n')]
        self.cols = [list(column) for column in zip(*self.rows)]

    def row(self, index=1):
        return self.rows[index-1]

    def column(self, index=1):
        return self.cols[index-1]