MyName = "Anthony"
age = 21
has_internship = True

def printing():
    return "Hi " + MyName

print(printing())

if age > 21:
    print("Allowed")
elif age == 21 and has_internship:
    print("That's Anthony")
else:
    print("We don't know him")

#List of users

users = [
    {"name": "Diamant Anthony", "role": "Intern", "email":"antho@gmail.com", "age":21},
    {"name": "Kylian MBAPPE", "role": "Pro Footballer", "email":"kyky@gmail.com", "age":27},
    {"name": "Terry Dubrow", "role": "Surgeon", "email":"terry@gmail.com", "age":68},
    {"name": "Dana White", "role": "CEO", "email":"dana@gmail.com", "age":49},
    {"name": "Tony Elumelu", "role": "Bank Chairman", "email":"tony@gmail.com", "age":68},
]

name = input("Enter your name: ")
email = input("Enter your email: ")
age = int(input("Enter your age: "))
role = input("Enter your role: ")
print("\n")

#Print myself
print("============ Printing my own name ============")
for user in users:

    if user["name"] == "Diamant Anthony" and user["email"] == "antho@gmail.com":
        print(user["name"])
print("\n")

print("============ Printing all users ============")
for user in users:
    #print(f"{user['name']} is a {user['role']}.")
    print(user["name"] + " is a " + user["role"] + ".")
print("\n")

print("============ You've entered the followings: ============")
print(name)
print(email)
print(age)
print(age)
