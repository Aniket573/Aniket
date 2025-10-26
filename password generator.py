import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print("Generated password:", generate_password(length))
input("\nPress enter to exit..")