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

def mat_add_sub(mat1, mat2, mode):
    mat1_shape = shape(mat1)
    mat2_shape = shape(mat2)
    if mat1_shape != mat2_shape:
        return ""
    else:
        matrix = []
        for i in range(mat1_shape[0]):
            line = []
            for j in range(mat2_shape[1]):
                if mode == "add":
                    line.append(mat1[i][j] + mat2[i][j])
                elif mode == "sub":
                    line.append(mat1[i][j] - mat2[i][j])
            matrix.append(line)
        return matrix

def mat_mul(mat1, mat2):
    mat1_shape = shape(mat1)
    mat2_shape = shape(mat2)
    if mat1_shape[1] != mat2_shape[0]:
        return ""
    else:
        matrix = []
        for i in range(mat1_shape[0]):
            line = []
            for j in range(mat2_shape[1]):
                term = 0
                for k in range(mat1_shape[1]):
                    term += mat1[i][k] * mat2[k][j]
                line.append(term)
            matrix.append(line)
        return matrix

a = input()
b = input()
A = to_matrix(a)
B = to_matrix(b)
print(mat_add_sub(A, B, "add"))
print(mat_add_sub(A, B, "sub"))
print(mat_mul(A, B))
print(mat_mul(B, A))
