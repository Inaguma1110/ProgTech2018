x = int(input())
y = int(input())
z = int(input())

def tarai(a, b, c):
    if a <= b:
        return b
    else:
        return tarai(
            tarai(a - 1, b, c), tarai(b - 1, c, a), tarai(c - 1, a, b))

print(tarai(x, y, z))
