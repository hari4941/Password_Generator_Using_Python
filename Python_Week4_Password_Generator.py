import random
import string

def generate_password(length=12):
    
    # Define the pool of characters to choose from
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Choose at least one character from each category
    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)
    password += random.choice(special_characters)

    # Choose remaining characters to fill up the password
    for i in range(length - 4):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    # Shuffle the password characters to randomize the order
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def generate_multiple_passwords(count=1, length=12):
    passwords = [generate_password(length) for i in range(count)]
    return passwords

if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the length of the password(s): "))
            if password_length < 4:
                print("Password must be greater than or equal to 4")
                continue
            password_count = int(input("Enter the number of password(s) to generate: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    passwords = generate_multiple_passwords(password_count, password_length)
    
    print("\nThe Generated Password(s):")
    for password in passwords:
        print(password)
