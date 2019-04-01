n = float(input())
if n > 1:
    x = n
else:
    x = 1
while True:
    f = x**2 - n
    f_dash = 2 * x
    if f < 10**(-8):
        break
    x = x - (f / f_dash)
print("%.4f" % x)
