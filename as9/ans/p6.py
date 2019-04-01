a = input()
b = input()
c = int(input())

def func(a, c, b=" "):
    for i in range(c):
        if i == c - 1:
            print(a)
        else:
            print(a, end=b)

func(a, c)
func(a, c, b)
