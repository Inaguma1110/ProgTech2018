def to_matrix(s):
    matrix = []
    for i in s.split(";"):
        line = []
        for j in i.split():
            line.append(int(j))
        matrix.append(line)
    return matrix

a = input()
print(to_matrix(a))
