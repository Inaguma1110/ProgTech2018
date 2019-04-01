class Matrix():
    def __init__(self, chars):
        self.chars = chars

    def to_matrix(self):
        chars = self.chars.split(';')
        matrix = []
        for char in chars:
            elements = char.split()
            line = [int(element) for element in elements]
            matrix.append(line)
        return matrix


chars = input()
matrix = Matrix(chars).to_matrix()
print(matrix)
