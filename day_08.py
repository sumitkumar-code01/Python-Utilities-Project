'''
    
    Challenge :Password Strength Checker & Suggestion Tool

    Build a Python Script that checks the strength of a given password
    based on :

    1. Lenght (At least 8 characters)
    2. Uppercase letters (At least one)
    3. Lowercase letters (At least one)
    4. Numbers (At least one)
    5. Special characters (e.g., !, @, #, $, etc.)

    
    Program Should :
    - Ask the user to input a password.    
    - Tell them Whats missing to make if it is weak.
    - if the password is strong, confirm it.
    - Suggest a strong password if the input is weak.

    
'''

import string
import random

# Function to suggest a strong password
def suggest_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    suggestion = "".join(random.choice(chars) for _ in range(12))
    return suggestion

# Function to check password strength
def check_password_strength(pwd):
    missing = []
    
    # Check length
    if len(pwd) < 8:
        missing.append("At least 8 characters")
    
    # Check for uppercase
    if not any(char.isupper() for char in pwd):
        missing.append("An uppercase letter")
        
    # Check for lowercase
    if not any(char.islower() for char in pwd):
        missing.append("A lowercase letter")
        
    # Check for digits
    if not any(char.isdigit() for char in pwd):
        missing.append("A number")
        
    # Check for special characters
    special_chars = "!@#$%^&*()-_+=<>?"
    if not any(char in special_chars for char in pwd):
        missing.append("A special character (!@#$ etc.)")

    # Final Result
    if not missing:
        print("\n Strength: Strong! Your password is secure.")
    else:
        print("\n Strength: Weak")
        print("Missing requirements:")
        for item in missing:
            print(f"  - {item}")
        
        print(f"\n Suggestion: Try something like '{suggest_password()}'")

# Main execution
def main():
    print(" Password Strength Checker & Suggestion Tool")
    user_pwd = input("Enter a password to check: ")
    check_password_strength(user_pwd)

if __name__ == "__main__":
    main()