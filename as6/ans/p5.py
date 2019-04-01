a = int(input())
b = int(input())

num_prime = 0

if a > b:
    a, b = b, a
for i in range(a, b + 1):
    num_diviser = 0
    for j in range(1, i + 1):
        if i % j == 0 and j != 1:
            num_diviser += 1
    if num_diviser == 1:
        num_prime += 1
print(num_prime)
