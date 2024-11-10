import random
import string
import hashlib
import pyperclip


def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    """
    Generates a random password with the specified length and character types.
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special else ""

    characters = lowercase + uppercase + digits + special_chars
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_boolean_input(prompt):
    """
    Prompts the user for a 'y' or 'n' response and returns True for 'y' and False for 'n'.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print("Error: Please enter 'y' for Yes or 'n' for No.")


def save_password_to_file(password, filename="password.txt"):
    """
    Saves the generated password to a file.
    """
    with open(filename, "w") as file:
        file.write(password)


def copy_to_clipboard(password):
    """
    Copies the generated password to the clipboard.
    """
    pyperclip.copy(password)


def check_password_strength(password):
    """
    Checks the strength of the password based on various criteria.
    """
    strength = 0

    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if len(password) >= 12:
        strength += 1

    if strength == 5:
        return "Very Strong"
    elif strength >= 4:
        return "Strong"
    elif strength >= 3:
        return "Medium"
    else:
        return "Weak"


def hash_password(password):
    """
    Hashes the password using SHA-256 and returns the hash.
    """
    return hashlib.sha256(password.encode()).hexdigest()

# Main program


def main():
    # Get user input for the desired password length
    while True:
        try:
            length = int(
                input("Enter the desired password length (between 8 and 16): "))
            if 8 <= length <= 16:
                break
            else:
                print("Error: Length must be between 8 and 16. Please try again.")
        except ValueError:
            print("Error: Please enter a valid number.")

    # Ask user for password criteria
    use_uppercase = get_boolean_input("Include uppercase letters? (y/n): ")
    use_numbers = get_boolean_input("Include numbers? (y/n): ")
    use_special = get_boolean_input("Include special characters? (y/n): ")

    # Generate and hash the password
    password = generate_password(
        length, use_uppercase, use_numbers, use_special)
    hashed_password = hash_password(password)

    # Display results
    print("-------------------------")
    print("Generated Password:", password)
    print("Password Strength:", check_password_strength(password))
    print("Hashed Password:", hashed_password)
    print("-------------------------")

    # Ask user if they want to save or copy the password
    action = input(
        "Do you want to save the password to a file (s) or copy to clipboard (c)? (s/c): ").lower()
    if action == 's':
        save_password_to_file(password)
        print("Password saved to 'password.txt'.")
    elif action == 'c':
        copy_to_clipboard(password)
        print("Password copied to clipboard.")
    else:
        print("Invalid option. No action taken.")


if __name__ == "__main__":
    main()
