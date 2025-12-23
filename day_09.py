'''
     Challenge: Set a Countdown Timer

    Create a Python script that allows the user to set a
    timer in seconds.

    Program Should:
    1. Ask the user for the number of seconds to set the timer
    2. Show a live countdown in the terminal.
    3. Notify the user when the timer ends with a final message and 
    sound (if possible).

'''

import time

def start_countdown():
    # 1. Ask the user for input
    print("--- PYTHON COUNTDOWN TIMER ---")
    try:
        user_input = input("Enter the time in seconds: ")
        seconds = int(user_input)

        # 2. Live Countdown Logic
        while seconds > 0:
            # Calculate minutes and seconds
            mins, secs = divmod(seconds, 60)
            
            # Format as MM:SS (02d means 2 digits)
            timer_format = f"{mins:02d}:{secs:02d}"
            
            # Print on the same line using \r
            print(f"Time Remaining: {timer_format}", end="\r")
            
            # Pause for 1 second
            time.sleep(1)
            
            # Reduce the count
            seconds -= 1

        # 3. Final Notification and Sound
        print("\n\n" + "="*20)
        print("STOP! THE TIMER ENDED.")
        print("="*20)
        
        # Triggering a system beep sound (ASCII Bell)
        print("\a" * 5) 

    except ValueError:
        print("Error: Please enter a valid whole number.")

# Run the function
if __name__ == "__main__":
    start_countdown()