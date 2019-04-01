class Integer:
    def __init__(self, value):
        self.__value = value

    def value(self):
        return self.__value


class String:
    def __init__(self, word):
        self.word = word

    def repeat_words(self, i):
        print(self.word * i.value())


a = input()
b = int(input())
str_a = String(a)
int_b = Integer(b)
str_a.repeat_words(int_b)
