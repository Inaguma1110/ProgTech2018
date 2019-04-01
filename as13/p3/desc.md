### 問題内容
第１１回課題の行列を作成する問題は，クラスを用いるを以下のように書き換えられる．  
以下のコードのコメントアウトで囲まれた`your code here`の部分で `__str__`メソッドをオーバーロードして，コードを完成させよ． （`_str__`メソッドは教科書p277を参照すること）

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
        return str(self.__matrix)
        '''
        your code here
        '''

A_str = input()
A = Matrix(A_str)
print(A)
```


### 入出力例
#### 入力例1
```
1 2 3;2 3 4
```

#### 出力例1
```
[[1, 2, 3], [2, 3, 4]]
```
#### 入力例2
```
1;2;3;4;5
```

#### 出力例2
```
[[1], [2], [3], [4], [5]]
```

### 注意事項

- ファイル名およびコード内（コメントも含む）に全角文字は使わない  
- ローカル環境（自分のPC）で実行結果が合っていることを確認してから提出する
