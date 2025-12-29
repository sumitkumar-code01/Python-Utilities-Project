'''
 Challenge : Emoji Enhancer for messages
 
 Create a Python script that takes a message
 and adds emojis after specific keyword to make it more expressive.

 Program Should :
 1. Ask the user to input a message.
 2. Add emojis after certain keywords(ike "happy", "love",
 "code", "tea", etc.).
 3. Print the enhanced message with emojis.


'''
# --- Challenge: Emoji Enhancer for Messages (Advanced) ---

# Humne ek 'Dictionary' banayi hai keywords aur emojis ko store karne ke liye
emoji_map = {
    "happy": "😊",
    "love": "❤",
    "code": "💻",
    "tea": "☕",
    "coffee": "☕",
    "fire": "🔥",
    "party": "🥳",
    "cool": "😎",
    "sad": "😢"
}


print("   DYNAMIC EMOJI........ ")

# 1. User se message input lena
original_text = input("Enter your message: ")

# Message ko words mein todna (Split karna) taaki hum har word ko check kar sakein
words = original_text.split()
result_words = []

# 2. Loop aur If statement ka use
for word in words:
    # Word ko lowercase mein convert karke check karenge (taaki 'Happy' bhi match ho jaye)
    clean_word = word.lower().strip(",.!?") 
    
    if clean_word in emoji_map:
        # Agar word dictionary mein hai, toh emoji ke saath add karo
        emoji = emoji_map[clean_word]
        result_words.append(f"{word} {emoji}")
    else:
        # Agar nahi hai, toh word ko waise hi rehne do
        result_words.append(word)

# 3. Words ko wapas jod kar sentence banana
final_message = " ".join(result_words)

print("\n--- Processing Complete ---")
print(f"Result: {final_message}")
