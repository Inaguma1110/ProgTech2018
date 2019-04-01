s = input()
freq_dict = {}
order_dict = {}
for c in s:
    if c in freq_dict:
        freq_dict[c] += 1
    else:
        freq_dict[c] = 1

    if not c in order_dict:
        order_dict[c] = len(order_dict) + 1

def func(dict_):
    max_value = 0
    for i, j in dict_.items():
        if j > max_value:
            max_value = j
            key_of_max_value = i
    print(key_of_max_value)


func(freq_dict)
func(order_dict)
