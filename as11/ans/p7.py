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


def mat_pow(array, n):
    if n == 1:
        return array
    elif n % 2 == 0:
        return mat_pow(mat_mul(array, array), n // 2)
    else:
        return mat_mul(array, mat_pow(array, n - 1))


a = input()
n = int(input())
A = to_array(a)
print(mat_pow(A, n))
