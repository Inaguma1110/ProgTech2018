class Message:
    def __init__(self, s):
        self.value = s


a = input()
message = Message(a)
print(message.value)
