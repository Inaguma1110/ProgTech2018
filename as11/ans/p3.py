def to_array(s):
    array = []
    for si in s.split(";"):
        tmp = []
        for sj in si.split(" "):
            tmp.append(int(sj))
        array.append(tmp)
    return array


def parse_shape(s):
    shape = []
    for i in s.split(" "):
        shape.append(int(i))
    return shape


def reshape(array, shape):
    flattend = []
    for column_lst in array:
        for v in column_lst:
            flattend.append(v)
    new_array = []
    k = 0
    for i in range(shape[0]):
        tmp = []
        for j in range(shape[1]):
            tmp.append(flattend[k])
            k += 1
        new_array.append(tmp)

    return new_array


A = to_array(input())
a, b = parse_shape(input())

print(reshape(A, (a, b)))
