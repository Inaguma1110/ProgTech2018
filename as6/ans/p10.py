a = int(input())
cnt = 0
k = 1  # current line
for i in range(1, a + 1):
    cnt += 1
    if cnt == k:
        k += 1
        cnt = 0
        print(i)
    else:
        print(i, end=" ")
