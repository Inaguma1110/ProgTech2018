import random

p = 3
for i in range(1, 6):
    f_in = open('p{}/in/input{}.txt'.format(p, i), mode='w')
    f_out = open('p{}/out/output{}.txt'.format(p, i), mode='w')

    input_lst = []
    for j in range(1):
        rand = random.randint(1, 100)
        input_lst.append(rand)
        f_in.write(str(rand) + '\n')

    for j in input_lst:
        sum_ = 0
        for x in range(1, j+1):
            sum_ += x
        f_out.write(str(sum_) + '\n')

    f_in.close()
    f_out.close()
