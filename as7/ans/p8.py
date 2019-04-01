A = set()
B = set()
for i in range(5):
    A.add(int(input()))
for i in range(5):
    B.add(int(input()))
print(A | B)
if len(A - B) > 0:
    print(A - B)
if len(A & B) > 0:
    print(A & B)
if len(A ^ B) > 0:
    print(A ^ B)
