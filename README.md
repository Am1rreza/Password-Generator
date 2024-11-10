# Password Generator

This is a simple Python-based password generator that allows users to generate secure passwords with customizable criteria. It provides functionality to:
- Generate passwords with a combination of uppercase letters, lowercase letters, digits, and special characters.
- Check the strength of the generated password.
- Save the password to a text file.
- Copy the password to the clipboard.

## Features

- **Customizable Password Length**: Choose a password length between 8 and 16 characters.
- **Character Set Customization**: Choose whether to include uppercase letters, numbers, and special characters.
- **Password Strength Checker**: The generated password's strength is evaluated based on its complexity.
- **Password Storage Options**: Save the password to a file or copy it directly to the clipboard for easy use.

## Requirements

- Python 3.x
- `pyperclip` library (used for copying to clipboard)

You can install the required library using pip:

```bash
pip install pyperclip
```

## Usage

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/am1rreza/password-generator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd password-generator
    ```

3. Run the `password_generator.py` script:
    ```bash
    python password_generator.py
    ```

4. Follow the on-screen prompts to customize the generated password:
    - Choose the password length.
    - Select whether to include uppercase letters, numbers, and special characters.
    - Once the password is generated, you can choose to either save it to a file or copy it to your clipboard.

## Example Output

```bash
Enter the desired password length (between 8 and 16): 12
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

-------------------------
Generated Password: Z2v$Lg5b8XpZ
-------------------------
Password Strength: Strong
-------------------------
Hashed Password: 2f9b4d3ed0f27fc7f7fd4a98c474b4d0b1b13c04b9a3e87f55b0e2c5dcb0e1a1
-------------------------
Do you want to save the password to a file (s) or copy to clipboard (c)? (s/c): s
Password saved to 'password.txt'.
```

## How It Works

- **Password Generation**: The program generates a random password based on the user's selected criteria (length, inclusion of uppercase letters, digits, special characters).
- **Password Strength**: The strength of the generated password is evaluated based on:
  - The presence of different types of characters (lowercase, uppercase, digits, special characters).
  - The length of the password.
- **Password Storage**: The user can choose to either save the generated password to a file or copy it to the clipboard using the `pyperclip` library.

## License

This project is open source and available under the [MIT License](LICENSE).
