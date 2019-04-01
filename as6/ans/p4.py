a = int(input())
b = int(input())
c = int(input())

mini = 1
if a >= b:
    if b > c:
        mini = c
    else:
        mini = b
else:
    if a > c:
        mini = c
    else:
        mini = a
num_div = 0  # divisor
gcd = 0  # greatest common divisor
for i in range(1, mini + 1):
    if a % i == 0 and b % i == 0 and c % i == 0:
        num_div += 1
        gcd = i
print(num_div, gcd)
