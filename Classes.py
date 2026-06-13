class Human:
    def __init__(self, name, age, gender, height, weight, nationality):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.nationality = nationality

    def display_info(self):
        print(" My name is " + self.name + ", I am " + self.nationality + ".")
        print(" I am a " + str(self.age) + " year old " + self.gender + " standing " + self.height + " weighing at " + str(self.weight) + " pound.")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender(Male or Female): ")
height = input("Enter your height(eg 6'1): ")
weight = float(input("Enter your weight(in lbs): "))
nationality = input("Enter your nationality(eg American): ")

#The Human object
person = Human(name, age, gender, height, weight, nationality)
person.display_info()