class Matrix():
    def __init__(self, ss):
        if isinstance(ss, str):
            self.__matrix = Matrix.__to_array(ss)
        else:
            self.__matrix = ss
        self.__rows = len(self.__matrix)
        self.__cols = len(self.__matrix[0])
 
    @staticmethod
    def __to_array(ss):
        a = []
        for si in ss.split(";"):
            ai = []
            for x in si.split():
                ai.append(int(x))
            a.append(ai)
        return a
   
    def matrix(self): return self.__matrix
    def rows(self): return self.__rows
    def cols(self): return self.__cols
    
    def __str__(self):
        return str(self.__matrix)

    def __mul__(self, matrix):
        mul_matrix = []
        for i in range(self.rows()):
            mul_matrix_i = []
            for j in range(matrix.cols()):
                term = 0
                for k in range(self.rows()):
                    term += self.matrix()[i][k] * matrix.matrix()[k][j]
                mul_matrix_i.append(term)
            mul_matrix.append(mul_matrix_i)
        return Matrix(mul_matrix)

def mat_power(mat, n):
    result = mat
    for i in range(n-1):
        result *= mat
    return result

A = Matrix([[1,1],[1,0]])
B = Matrix([[1],[0]])
n = int(input())
A_n = mat_power(A, n)
ans = A_n * B
print(ans.matrix()[1][0])
