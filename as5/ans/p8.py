x = int(input())

cnt = 0
for a in range(11):
    for b in range(11):
        for c in range(11):
            if 50 * a + 10 * b + 5 * c == x:
                cnt += 1
print(cnt)
