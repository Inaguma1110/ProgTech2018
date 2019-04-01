a = int(input())

b = [0, 1]

if a % 2 == 0:
    c = [0, 1] * a
else:
    c = [[0, 1]] * a

print(c)
