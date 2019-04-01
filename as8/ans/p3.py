x = input()
a = []
while x != "end":
    a.append(int(x))
    x = input()
b = a[:]
b[0] += 1
c = a[:]
c[0] -= 1
print(b + c)
