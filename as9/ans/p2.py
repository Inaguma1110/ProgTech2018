s = input()
a = int(input())
b = int(input())

def func(s, a, b):
    if a <= len(s) and b <= len(s):
        return (s[a - 1], s[b - 1])
    else:
        return s

print(func(s, a, b))
