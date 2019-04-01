class Integer:
    def __init__(self, v):
        self.v = v
    def add(self, i):
        result = self.v + i.v
        return Integer(result)

a = int(input())
b = int(input())
a_i = Integer(a)
b_i = Integer(b)
sum_i = a_i.add(b_i)
print(sum_i.v)
        
