a = int(input())
b = int(input())
c = int(input())

if b < a and c < a:
    a, c = c, a
elif a < b and c < b:
    b, c = c, b

if a + b == c:
    print(c)
else:
    print("neq")
