class Human:
    def __init__(self, name, age, gender, height, weight, nationality):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.nationality = nationality

    def display_info(self):
        print("============= PERSONAL INFORMATION =============")
        print(" My name is " + self.name + ", I am " + self.nationality + ".")
        print(" I am a " + str(self.age) + " year old " + self.gender + " standing " + self.height + " weighing at " + str(self.weight) + " pound.")
        print("\n")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender(Male or Female): ")
height = input("Enter your height(eg 6'1): ")
weight = float(input("Enter your weight(in lbs): "))
nationality = input("Enter your nationality(eg American): ")
print("\n")

#The Human object
person = Human(name, age, gender, height, weight, nationality)
person.display_info()

class User:
    def __init__(self, u_name, u_role, u_age):
        self.u_name = u_name
        self.u_role = u_role
        self.u_age = u_age

    def greet(self):
        print(f"Hi, I am {self.u_name} and I am {self.u_role}.")

    def is_adult(self):
        if self.u_age >= 18:
            print(self.u_name + " is an adult.")
        else:
            print(self.u_name + " is a minor.")

    def describe(self):
        status = "adult" if self.u_age >= 18 else "minor"
        print(f"{self.u_name} is  {status}, age {self.u_age}.")

#u_name = input("Enter your names: ")
#u_role = input("Enter your role: ")
#u_age = int(input("Enter your age: "))

userA = User("Diamant Anthony", "Intern", 21)
userB = User("Tony O. Elumelu", "Chairman", 21)
userC = User("Mark", "Student", 17)
userD = User("Ralph", "Freelance", 18)

#Fixing missing C and D users
print("=============== USING Object ===============")
userA.greet()
userB.greet()
userC.greet()
userD.greet()
print("=============================================")
userA.is_adult()
userB.is_adult()
userC.is_adult()
userD.is_adult()
print("=============================================")
userA.describe()
userB.describe()
userC.describe()
userD.describe()