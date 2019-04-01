def func(*args, mode="add"):
    if mode == "add":
        ans = 0
        for i in args:
            ans += i
    elif mode == "prod":
        ans = 1
        for i in args:
            ans *= i
    print(ans)


func(1, 2, 3, 4, 5)
func(2, 3, mode="prod")
