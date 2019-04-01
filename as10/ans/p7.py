x = int(input())
y = int(input())
z = int(input())

MEMO = {}

def tarai(a, b, c):
    if a <= b:
        return b
    else:
        if (a, b, c) in MEMO:
            return MEMO[(a, b, c)]
        t = tarai(tarai(a - 1, b, c), tarai(b - 1, c, a), tarai(c - 1, a, b))
        MEMO[(a, b, c)] = t
        return t

print(tarai(x, y, z))
