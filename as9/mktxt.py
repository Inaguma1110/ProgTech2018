import random

p = 1
for i in range(1, 6):
    f_in = open('p{}/in/input{}.txt'.format(p, i), mode='w')
    f_out = open('p{}/out/output{}.txt'.format(p, i), mode='w')

    input_lst = []
    for j in range(2):
        rand = random.randint(1, 100)
        input_lst.append(rand)
        f_in.write(str(rand) + '\n')
    output = 0
    for x in input_lst:
        output += x
    f_out.write(str(output))

    f_in.close()
    f_out.close()
