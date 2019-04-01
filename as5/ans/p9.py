a = int(input())
s = ""
while a > 0:
    b = a % 2
    a //= 2
    s = str(b) + s
print(s)
