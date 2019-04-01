a = int(input())
b = int(input())
sum_ab = 0
if a > b:
    for i in range(b, a + 1):
        sum_ab += i
else:
    for i in range(a, b + 1):
        sum_ab += i
print(sum_ab)
