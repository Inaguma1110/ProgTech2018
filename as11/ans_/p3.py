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

def reshape(matrix, tpl):
    flattened = []
    for x in matrix:
        flattened += x
    k = 0
    new_matrix = []
    for i in range(tpl[0]):
        new_line = []
        for j in range(tpl[1]):
            new_line.append(flattened[k])
            k += 1
        new_matrix.append(new_line)
    return new_matrix
    
a = input()
s = input()
new_shape = tuple(map(lambda x: int(x), s.split()))
print(reshape(to_matrix(a), new_shape))
