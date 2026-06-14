class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi, I am " + self.name)

# Employee INHERITS from Human
class Employee(Human):
    def __init__(self, name, age, role, salary):
        # calls Human's __init__
        super().__init__(name, age)
        self.role = role
        self.salary = salary

    def describe(self):
        print(self.name + " is a " + self.role + " earning $" + str(self.salary))

emp = Employee("Diamant Anthony", 21, "Intern", 500)
emp.greet()
emp.describe()

class Aircraft:
    def fly(self):
        print("I fly")

class Airbus(Aircraft):
    def fly(self):
        print("I am a A350")

airbus = Airbus()
airbus.fly()

class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    @staticmethod
    def app_name():
        print("MyApp v1.0")

    @classmethod
    def total_users(cls):
        print("Total Users: " + str(cls.count))

User("Diamant Anthony")
User("Tony O. Elumelu")
User.total_users()
User.app_name()