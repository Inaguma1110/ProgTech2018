chars = input()
alp = 0
num = 0
for char in chars:
    if "A" <= char <= "Z" or "a" <= char <= "z":
        alp += 1
    elif "0" <= char <= "9":
        num += 1
    else:
        pass
print(num, alp)
