sum_end = 0
flg = 0
while True:
    x = input()
    if x == "end":
        if flg == 0:
            sum_end = "None"
        break
    else:
        flg = 1
        x = int(x)
        sum_end += x
print(sum_end)
