a = input()
d = int(input())

def to_list(a):
    b = a.split()
    for i in range(len(b)):
        b[i] = int(b[i])
    return b

def get_max(b):
    c = sorted(b)
    return c[-1]

def power(c, d):
    e = []
    for i in range(d + 1):
        f = c**i
        e.append(f)
    return (e)

b = to_list(a)
c = get_max(b)
print(power(c, d))
