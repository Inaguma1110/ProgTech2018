a = input()
l = []
while a != "end":
    l.append(int(a))
    a = input()
s = set(l)
s.remove(l[-1])

if len(s) > 0:
    print(s)


