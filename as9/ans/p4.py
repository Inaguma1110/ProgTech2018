a = input()

def to_list(a):
    b = a.split()
    for i in range(len(b)):
        b[i] = int(b[i])
    return b

def get_max(b):
    c = sorted(b)
    return c[-1]

b = to_list(a)
print(get_max(b))
