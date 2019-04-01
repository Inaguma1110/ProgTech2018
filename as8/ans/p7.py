words = input().split()
lc = {}
for word in words:
    key = word[0].upper()
    lc[key] = word
for k, v in sorted(lc.items()):
    print("{}:{}".format(k, v), end=" ")
