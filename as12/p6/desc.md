### 問題内容
整数`a`を受け取り，一辺の長さが'a'の正方形の面積を出力するプログラムを記述せよ.
ただし，以下のコードのコメントアウトで囲まれたyour code hereの部分のみを変更することにより，プログラムを完成させること．
変更したあとはコメントアウトを外すこと．


```
a = int(input())
class rectangle:
    def __init__(self, w, h):
        self.w = w
	self.h = h
    def area(self):
        return self.w * self.h
class square(rectangle):
    '''
    your code here
    '''
s = square(a)
print(s.area())
```

### 入出力例
#### 入力例1
```
2
```

#### 出力例1
```
4
```
#### 入力例2
```
3
```

#### 出力例2
```
9
```

### 注意事項

- ファイル名およびコード内（コメントも含む）に全角文字は使わない  
- ローカル環境（自分のPC）で実行結果が合っていることを確認してから提出する
