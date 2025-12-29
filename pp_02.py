'''
Challenge : Stylish Bio Generator for Instagram/Twitter

Create a python utility that asks the user for a few key
details and generates a short, stylish bio that couid be used
for social media profiles line Instagram or twitter.

Program should :
1. Prompt the user to enter their :
   - Name
   - Profession
   - One-Liner passion or goal
   - Faviorite emoji
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs.
   it should feel modern, concise, and catchy.

3. Add optional hastags or emojis for flair.

'''
def stylish_bio_generator():
    print("\n--- ✨ Stylish Bio Generator ✨ ---")
    print("Answer a few questions to create your perfect social media bio.\n")

    # 1. Prompting user for inputs
    name = input("Enter your Name: ").strip()
    profession = input("Enter your Profession: ").strip()
    goal = input("Enter your One-Liner passion or goal: ").strip()
    emoji = input("Enter your favorite emoji: ").strip()
    website = input("Enter your Website or handle (optional): ").strip()

    # 2. Building the Bio string
    line1 = f"{emoji} | {name.title()}"
    line2 = f"🚀 {profession.title()} | {goal.capitalize()}"
    link = f"🔗 {website}" if website else ""
    hashtags = f"#{profession.replace(' ', '')} #Success #Vibes"
    
    # Combine everything into one variable for printing and saving
    full_bio = f"{line1}\n{line2}\n{link}\n{hashtags}" if website else f"{line1}\n{line2}\n{hashtags}"

    # 3. Printing the Bio
    print("\n" + "-"*50)
    print("YOUR NEW BIO:")
    print("-"*50)
    print(full_bio)
    print("-" * 50)

    # 4. Saving logic (Inside the function so it can access 'name' and 'full_bio')
    save = input("Do you want to save this bio to a text file? (y/n): ").lower()
    if save == 'y':
        filename = f"{name.lower().replace(' ', '_')}_bio.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_bio)
        print(f"✅ Success! Saved as: {filename}")
    else:
        print("❌ File not saved.")

# RUN the program
if __name__ == "__main__":
    stylish_bio_generator()