# main.py

from models.user import User
from utils.helpers import print_separator, print_all_users

# Create users
userA = User("Diamant Anthony", "Intern", 21)
userB = User("Tony Elumelu", "Chairman", 61)
userC = User("Kylian Mbappe", "Footballer", 27)

users = [userA, userB, userC]

# Use helper functions
print_separator("ALL USERS")
print_all_users(users)

print_separator("DESCRIPTIONS")
for user in users:
    user.describe()