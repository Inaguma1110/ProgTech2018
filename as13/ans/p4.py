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

    def reshape(self, rows, cols):
        new_matrix = []
        new_row = []
        for row in self.__matrix:
            for element in row:
                new_row.append(element)
                if len(new_row) == rows:
                    new_matrix.append(new_row)
                    new_row = []
        return Matrix(new_matrix)

A = Matrix(input())
x, y = map(int, input().split())
A_new = A.reshape(x, y)
print(A_new)
