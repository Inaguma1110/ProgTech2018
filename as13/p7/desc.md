### 問題内容
フィボナッチ数列は以下のように表すことができる．  

整数nを受け取り，フィボナッチ数列の第n項を行列のべき乗を用いて求めるプログラムを記述せよ．  
以下のコードのコメントアウトで囲まれた`your code here`の部分のみを変更することにより，プログラムを完成させること．

### ヒント

```
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
        '''
        your code here
        '''

    def reshape(self, rows, cols):
        '''
        your code here
        '''

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
    '''
    your code here
    '''

'''
your code here
'''
```

### 入出力例
#### 入力例1
```
2
```
#### 出力例1
```
1
```

#### 入力例1
```
10
```
#### 出力例1
```
55
```
### 注意事項

- ファイル名およびコード内（コメントも含む）に全角文字は使わない  
- ローカル環境（自分のPC）で実行結果が合っていることを確認してから提出する
