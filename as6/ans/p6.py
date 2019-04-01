a = input()
b = input()

if "1" <= a <= "9":
    if "1" <= b <= "9":
        print(int(a) + int(b))
    else:
        for i in range(int(a)):
            print(b)

else:
    if "1" <= b <= "9":
        for i in range(int(b)):
            print(a)
    else:
        if a < b:
            print(a)
            print(b)
        else:
            print(b)
            print(a)
