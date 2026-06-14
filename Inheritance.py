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