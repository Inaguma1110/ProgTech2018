def a(n):
    if n == 1:
        return 1
    return 3 * a(n - 1) + 2 * (n - 1) + 1


n = int(input())
print(a(n))
