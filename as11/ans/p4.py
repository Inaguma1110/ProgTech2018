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


def mat_add(array1, array2):
    if get_shape(array1) != get_shape(array2):
        return None
    else:
        result = []
        shape = get_shape(array1)
        for i in range(shape[0]):
            tmp = []
            for j in range(shape[1]):
                tmp.append(array1[i][j] + array2[i][j])
            result.append(tmp)
        return result


def mat_sub(array1, array2):
    if get_shape(array1) != get_shape(array2):
        return None
    else:
        result = []
        shape = get_shape(array1)
        for i in range(shape[0]):
            tmp = []
            for j in range(shape[1]):
                tmp.append(array1[i][j] - array2[i][j])
            result.append(tmp)
        return result


def mat_mul(array1, array2):
    if get_shape(array1)[1] != get_shape(array2)[0]:
        return None
    else:
        result = []
        shape1 = get_shape(array1)
        shape2 = get_shape(array2)
        for i in range(shape1[0]):
            tmp = []
            for j in range(shape2[1]):
                v = 0
                for k in range(get_shape(array1)[1]):
                    v += array1[i][k] * array2[k][j]
                tmp.append(v)
            result.append(tmp)
        return result


a = input()
b = input()
A = to_array(a)
B = to_array(b)
add_result = mat_add(A, B)
if add_result is None:
    print("")
else:
    print(add_result)
sub_result = mat_sub(A, B)
if sub_result is None:
    print("")
else:
    print(sub_result)
mul_result1 = mat_mul(A, B)
if mul_result1 is None:
    print("")
else:
    print(mul_result1)
mul_result2 = mat_mul(B, A)
if mul_result2 is None:
    print("")
else:
    print(mul_result2)
