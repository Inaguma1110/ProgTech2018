import random

p = 1
for i in range(1, 6):
    f_in = open('p{}/in/input{}.txt'.format(p, i), mode='w')
    f_out = open('p{}/out/output{}.txt'.format(p, i), mode='w')
    lst = []
    for j in range(1):
        rand = random.randint(1, 100)
        f_in.write(str(rand))

    '''
    a = rand
    k = 0
    line = 1
    for i in range(1, a+1):
        k += 1
        if k == line:
            line += 1
            k = 0
            #print(i)
            f_out.write(str(i)+'\n')
        else:
            f_out.write(str(i)+' ')
            #print(i, end=" ")
    '''
    x = rand
    for i in range(x+1):
        f_out.write(str(i)+'\n')

    f_in.close()
    f_out.close()
