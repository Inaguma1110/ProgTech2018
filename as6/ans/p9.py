chars = input()
sum_char = 0
flg = 0
for char in chars:
    if flg == 1 and "0" <= char <= "9":
        sum_char += int(char)
    flg = 0
    if char == "\"":
        flg = 1
print("\'" + str(sum_char) + "\'")
