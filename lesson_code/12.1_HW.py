class User:

    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f"Приветствую, {self.name}!"


def welcome():
    user = User(input("Как тебя зовут?\n"))
    return user.greetings()
