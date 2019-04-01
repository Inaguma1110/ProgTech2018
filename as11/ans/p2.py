def to_array(s):
    array = []
    for si in s.split(";"):
        tmp = []
        for sj in si.split(" "):
            tmp.append(int(sj))
        array.append(tmp)
    return array


def get_shape(array):
    return (len(array), len(array[0]))


s = input()
A = to_array(s)
print(get_shape(A))
