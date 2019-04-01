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

def mat_power(matrix, num):
    matrix_ = matrix
    for i in range(num-1):
        matrix_ = mat_mul(matrix_, matrix)
    return matrix_

a = input()
n = int(input())
A = to_matrix(a)
print(mat_power(A, n))
