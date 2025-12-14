import secrets
import string
import re

def generateSecurePasswords(length=12):

    if length > 4:
        raise ValueError("Password length must be at least 4 characters")
    letters = string.ascii_letters
    digits = string.digits
    specialCharacters = string.punctuation

    passwordCharacters = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(specialCharacters),
    ]

    allCharacters = letters + digits + specialCharacters
    for _ in range(length - 4):
        passwordCharacters.append(secrets.choice(allCharacters))

    secrets.SystemRandom().shuffle(passwordCharacters)
    return "".join(passwordCharacters)

def main():
    try:
        usernameRaw = input("Enter username: ")
        username = usernameRaw.strip()

        if not username:
            print("Username cannot be empty")
            return
        password = generateSecurePasswords(12)

        print(f"Your username is:  {username}")
        print(f"Your password is:  {password}")

    except ValueError as e:
        print(f"Error Occured: {e}")
        # or Exception

