### 問題内容
たらいまわし関数（竹内関数）は3つの引数をとる次のような関数である．  
\\(\mathrm{Tarai}(x,\ y,\ z) = \begin{cases} y & (if\ x \leq y) \\\ \mathrm{Tarai}(\mathrm{Tarai}(x-1,\ y,\ z),\ \mathrm{Tarai}(y-1,\ z,\ x),\ \mathrm{Tarai}(z-1,\ x,\ y)) & (otherwise) \end{cases}\\)  
正の整数 \\(x,\ y,\ z\\) を受け取り，\\(\mathrm{Tarai}(x,\ y,\ z)\\) を出力するプログラムを記述せよ．  
ただし， \\(x,\ y,\ z\ \leq 10\\) とする．

### 入出力例
#### 入力例1
```
10
5
0
```

#### 出力例1
```
10
```

#### 入力例2
```
8
0
4
```

#### 出力例2
```
4
```

### 注意事項

- ファイル名およびコード内（コメントも含む）に全角文字は使わない  
- ローカル環境（自分のPC）で実行結果が合っていることを確認してから提出する