'''
Challenge : Self_Into Script Generator 

Create a python scipt that interacts with the use 
and generates a personalized self_introdection

 '''
# Ask user for details
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
profession = input("Enter your profession: ")
hobby = input("Enter your favorite hobby: ")

# Print a warm self-introduction
print("\n--- Self Introduction ---\n")
print(f"Hello! My name is {name}. I am {age} years old and I live in {city}. "
      f"I work as a {profession}, and in my free time, I really enjoy {hobby}. "
      "Nice to meet you!")  

