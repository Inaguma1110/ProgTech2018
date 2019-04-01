class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is {}.".format(self.name))


a = input()
person = Person(a)
person.introduce()
