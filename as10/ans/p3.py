n = int(input())

def sum_upto(x):
    if x == 1:
        return 1
    else:
        return x + sum_upto(x - 1)

print(sum_upto(n))
