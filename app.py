import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if length < 4:
        raise ValueError("The length must be at least 4 to ensure a secure password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example of usage
if __name__ == "__main__":
    print("Password Generator")
    length = int(input("Password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    try:
        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        print(f"Your generated password: {password}")
    except ValueError as e:
        print(e)
