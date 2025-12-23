'''

Building a Caesar Cipher

     Challenge : Secret Message Encryptor & Decryptor

     Create a Python Script that helps you send secret messages
     to your friends using simple encryption.

     Program Should :
     1. Ask the user if they want to encrypt or decrypt a message.
     2. If encrypting :
        - Ask for the message and a numeric secret key.
        - Use a Caesar cipher (shift each letter by the key value).
        - Display the encrypted message.
     3. If decrypting :
        - Ask for the encrypted message and a numeric secret key.
        - Reverse the encryption to get the original message 


         
'''


# Day 10 Challenge: Caesar Cipher Project

def start_program():
    print("Secret message program")
    
    while True:
        # Prompt user for mode as seen in the terminal image
        mode = input("Do you want to E or DE (or type 'exit'): ").upper()
        
        if mode == 'EXIT':
            print("Shutting down...")
            break
            
        if mode == 'E' or mode == 'DE':
            message = input("Enter your message: ")
            
            # Using try-except to catch non-integer inputs for the key
            try:
                shift = int(input("Enter a number between 1 and 25: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value for the key.")
                continue

            if mode == 'DE':
                shift = -shift

            translated_text = ""

            for char in message:
                if char.isalpha():
                    # Determine the ASCII starting point (A=65, a=97)
                    ascii_offset = ord('A') if char.isupper() else ord('a')
                    
                    # Apply Caesar Cipher formula: (Position + Shift) % 26
                    new_char_code = (ord(char) - ascii_offset + shift) % 26
                    translated_text += chr(new_char_code + ascii_offset)
                else:
                    # Keep spaces and special characters as they are
                    translated_text += char

            # Display the final output based on the chosen mode
            if mode == 'E':
                print("Encrypted message:")
            else:
                print("Decrypted message:")
                
            print(f"{translated_text}\n")
        else:
            print("Please enter 'E' for encryption or 'DE' for decryption.")


if __name__ == "__main__":
    start_program()

