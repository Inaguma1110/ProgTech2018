import random

p = 6
for i in range(1, 11):
    f_in = open('p{}/in/input{}.txt'.format(p, i), mode='w')
    f_out = open('p{}/out/output{}.txt'.format(p, i), mode='w')
    lst = []
    for j in range(3):
    #for j in range(1):
        #rand = random.randint(-100, 100)
        rand = random.uniform(-5, 5)
        lst.append(rand)
        f_in.write(str(rand) + '\n')
    a, b, c = lst
    #a = lst[0]

    '''
    if a % 3 == 0 and a % 5 == 0:
        f_out.write("FizzBuzz")
    elif a % 3 == 0:
        f_out.write("Fizz")
    elif a % 5 == 0:
        f_out.write("Buzz")
    else:
        f_out.write(str(a))

    if a <= b <= c:
        f_out.write(str(b))
    elif a <= c <= b:
        f_out.write(str(c))
    elif b <= a <= c:
        f_out.write(str(a))
    elif b <= c <= a:
        f_out.write(str(c))
    elif c <= a <= b:
        f_out.write(str(a))
    elif c <= b <= a:
        f_out.write(str(b))
    '''
    cnt = 0
    if a > 0:
        cnt += 1
    if b > 0:
        cnt += 1
    if c > 0:
        cnt += 1
    f_out.write(str(cnt))

    f_in.close()
    f_out.close()
