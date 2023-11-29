import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_multiple_passwords(num_passwords, length):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords


def main():
    print("Welcome to Strong Password Generator!")
    print("-----------------------------------")
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))

        if num_passwords <= 0 or password_length <= 0:
            print("Please enter valid numbers greater than zero.")
            return

        generated_passwords = generate_multiple_passwords(num_passwords, password_length)

        print("\nGenerated Passwords:")
        for i, password in enumerate(generated_passwords, start=1):
            print(f"Password {i}: {password}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    main()
