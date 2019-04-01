### 問題内容
`Matrix`クラスに`reshape`メソッドを追加せよ．  
`reshape`メソッドは2つの正の整数（行数を列数）を引数にとり，reshapeしたMatrixインスタンスを戻すメソッドである．
以下のコードのコメントアウトで囲まれた`your code here`の部分のみを変更することにより，プログラムを完成させること．

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

A = Matrix(input())
x, y = map(int, input().split())
A_new = A.reshape()
print(A_new)
```

### 入出力例
#### 入力例1
```
1 2 3;2 3 4
3 2
```

#### 出力例1
```
[[1, 2], [3, 4], [5, 6]]
```

#### 入力例2
```
1;2;3;4;5
1 5
```

#### 出力例2
```
[[1, 2, 3, 4, 5]]
```



### 注意事項

- ファイル名およびコード内（コメントも含む）に全角文字は使わない  
- ローカル環境（自分のPC）で実行結果が合っていることを確認してから提出する
