def pow1(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow3(a * a, n / 2)
    else:
        if n < 0:
            return pow3(a, n + 1) / a
        else:
            return pow3(a, n - 1) * a


def pow2(a, n, r=1):
    if n == 0:
        return r
    elif n % 2 == 0:
        return pow2(a * a, n / 2, r)
    elif n % 2 == 1:
        if n < 0:
            return pow2(a, n + 1, r / a)
        else:
            return pow2(a, n - 1, r * a)


def pow3(a, n, r=1):
    if n == 0:
        return r
    elif n < 0:
        return 1 / pow3(a, -n, r)
    else:
        if n & 1:
            return pow3(a * a, n >> 1, r * a)
        else:
            return pow3(a * a, n >> 1, r)


a = int(input())
b = int(input())


def power(x, y):
    return pow3(x, y)


print(power(a, b))
