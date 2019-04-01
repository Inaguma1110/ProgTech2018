a = int(input())
b = int(input())

def power(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return power(x, y + 1) / x
    else:
        return power(x, y - 1) * x

print(power(a, b))
