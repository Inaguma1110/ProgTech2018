import random

p = 5
for i in range(1, 11):
    f_in = open('p{}/in/input{}.txt'.format(p, i), mode='w')
    f_out = open('p{}/out/output{}.txt'.format(p, i), mode='w')
    lst = []
    for j in range(1):
        rand = random.randint(0, 70)
        f_in.write(str(rand * 10))

    x = rand * 10
    cnt = 0
    for a in range(11):
        for b in range(11):
            for c in range(11):
                if 50 * a + 10 * b + 5 * c == x:
                    cnt += 1
    f_out.write(str(cnt))
    '''
    a = rand
    s = ""
    while a > 0:
        b = a % 2
        a //= 2
        s = str(b) + s
    f_out.write(s)
    '''

    f_in.close()
    f_out.close()
