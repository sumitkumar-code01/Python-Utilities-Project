'''  
    Challenge : Daily Journal Logger..

    Build a Python Script that llow you to maintain a daily
    learning journal. Each entry will be saved into a ' .text' file
    along with a timestamp.

    Program Should :
    1. Ask the user what they learned today.
    2. Add the entry to file called 'learning_journal.txt'.
    3. Each entry should include the date and time it was written.
    4. the program should append new entries rather than overwrite.

    bonus :
    - Add an optional rating (1-5) for how well productive the day was.
    - Show a confirmation message after saving the entry.
    - Make sure the format is clean and easy to read when opening 
    the file. 
'''


import datetime # Date aur time ke liye

def save_journal_entry():
    print("---  My Daily Learning Journal ---")
    
    # 1. User se input lena
    entry = input("\nWhat did you learn today? \n> ")
    rating = input("How productive was your day? (1-5): ")

    # Current date aur time nikalna
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S") # Format: YYYY-MM-DD HH:MM:SS

    # 2. File mein entry save karna (Append mode 'a' ka use karke)
    # Isse purana data delete nahi hoga, naya niche add hota jayega
    try:
        with open("learning_journal.txt", "a") as file:
            file.write(f"Date: {timestamp}\n")
            file.write(f"Productivity Rating: {rating}/5\n")
            file.write(f"Learned: {entry}\n")
            file.write("-" * 30 + "\n") # Divider line for clarity
        
        # Bonus: Confirmation message
        print("\n✅ Success! Your entry has been saved to 'learning_journal.txt'.")
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Program ko run karna
if __name__ == "__main__":
    save_journal_entry()