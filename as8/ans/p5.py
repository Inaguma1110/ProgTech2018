sentence = input().split()
tgt_word = input()
lc = {}
idx = 1
for w in sentence:
    lc[w] = idx
    idx += 1
if tgt_word in lc:
    print(lc[tgt_word])
