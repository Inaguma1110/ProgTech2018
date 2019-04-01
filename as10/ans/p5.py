n = int(input())

def recursion(x):
    if x == 1:
        return 3
    else:
        return 2 * recursion(x - 1) + (x - 1) + 1

print(recursion(n))
