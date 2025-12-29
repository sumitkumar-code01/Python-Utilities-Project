'''
Challenge : Minutes Alive Calculator

Write a python script that calculates approximately how many
minutes old a person is, based on their agee in years.

program Should :
1. Ask for the user's age in years.
2. Conert that age into :
    - Total days
    - Total hours
    - Total minutes

3. Display the results in a clear format.

assumptions :
- you can assume a year has 365.25 days/year to account for leap years.
- you dont need to handle time zones or exact birthdates in
this version.

'''

# --- Minutes Alive Calculator ---


print("   WELCOME TO THE LIFE CALCULATOR!    ")


# 1. User se age pucha ja raha hai
age = float(input("Enter your age in years: "))

# Hum assumptions ke hisaab se calculation kar rahe hain
# 1 Year = 365.25 Days
# 1 Day = 24 Hours
# 1 Hour = 60 Minutes

# 2. Conversion Logic
total_days = age * 365.25
total_hours = total_days * 24
total_minutes = total_hours * 60

# 3. Results ko display karna (formatted way mein)
print("\n--- Your Results ---")
print(f"Total Days lived    : {total_days:,.2f}")
print(f"Total Hours lived   : {total_hours:,.2f}")
print(f"Total Minutes lived : {total_minutes:,.2f}")
print("---------------------------------------")
print("Wow! You've lived a long time already!")