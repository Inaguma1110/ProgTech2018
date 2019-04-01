### 問題内容
半角スペースとセミころん`;`で区切られた文字列を受け取る。
この文字列からリストのリスト(行列)を返す関数を記述し、作成したリストを表示するプログラム（プログラムコード１）がある(課題11-1)。このプログラムをクラス`Matrix`を用いたプログラム（プログラムコード２）に当てはまるように`your code here`の部分のみを変更せよ.変更後は、コメントアウトを外すこと。

###プログラムコード1
```
chars = input()

def to_matrix(chars):
    chars = chars.split(';')
    matrix =[]
    for char in chars:
    	elements = char.split()
	line = [int(element) for element in elements]
	matrix.append(line)
    return matrix
matrix = to_matrix(chars)
print(matrix)

```
###プログラムコード2
```
class Matrix():
      def __init__(self, chars):
      	  '''
      	  your code here
	  '''
      def to_matrix(self):
      	  '''
	  your code here
	  '''

chars = input()
matrix = ``` your code here '''
print(matrix)

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
