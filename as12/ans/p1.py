start, end = map(int, input().split(","))
ans = 0

for i in range(start, end + 1):
    ans += i

print(ans)
