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
    if num == 1:
        return matrix
    elif num % 2 == 0:
        return mat_power(mat_mul(matrix, matrix), num//2)
    elif num % 2 == 1:
        return mat_mul(matrix, mat_power(matrix, num-1))

a = input()
n = int(input())
A = to_matrix(a)
print(mat_power(A, n))
