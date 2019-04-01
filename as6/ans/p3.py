sentence1 = input()
sentence2 = input()

common_char = 0
for char1 in sentence1:
    for char2 in sentence2:
        if char1 == char2:
            common_char += 1
print(common_char)
