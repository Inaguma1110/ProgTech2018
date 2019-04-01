a = int(input())

old = 1
fib = 1
for i in range(a):
    if i != 0 and i != 1:
        old2 = old
        old = fib
        fib = old + old2
    print(fib)
