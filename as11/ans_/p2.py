def to_matrix(s):
    matrix = []
    for i in s.split(";"):
        line = []
        for j in i.split():
            line.append(int(j))
        matrix.append(line)
    return matrix

def shape(matrix):
    return (len(matrix), len(matrix[0]))

a = input()
print(shape(to_matrix(a)))
