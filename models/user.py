
class User:
    def __init__(self, name, role, age):
        self.name = name
        self.role = role
        self.age = age

    def greet(self):
        print("Hi, I am " + self.name + " and I am a " + self.role)

    def describe(self):
        status = "an adult" if self.age >= 18 else "a minor"
        print(self.name + " is " + status + ", age " + str(self.age))