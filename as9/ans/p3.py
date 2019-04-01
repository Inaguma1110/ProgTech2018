a = input()

def to_list(a):
    b = a.split()
    for i in range(len(b)):
        b[i] = int(b[i])
    return b

print(to_list(a))
