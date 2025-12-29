'''
challenge : Simple Bill Splitter

Write a python script that helps split a bill evenly between
friends.

Program Should :
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share the bill.
5. Display how much each person owes in a clear format.


'''

def bill_splitter():
    print("--- 💸 Smart Bill Splitter 💸 ---")
    
    try:
        # 1. Ask for group size
        num_people = int(input("How many people are in the group? "))
        
        # 2. Ask for each person's name using a list
        names = []
        for i in range(num_people):
            name = input(f"Enter name for person {i+1}: ").strip().title()
            names.append(name)
            
        # 3. Ask for total bill amount
        total_bill = float(input("Enter the total bill amount (₹): "))
        
        # 4. Calculate share
        # We use standard division: total / number of people
        share = total_bill / num_people
        
        # 5. Display results in a clean format
        print("\n" + "="*30)
        print(f"💰 TOTAL BILL: ₹{total_bill:,.2f}")
        print(f"👥 SPLIT BETWEEN: {num_people} friends")
        print("="*30)
        
        for name in names:
            print(f"✅ {name:15} owes: ₹{share:,.2f}")
            
        print("="*30)
        print("Hope you had a great time! ✨")

    except ValueError:
        print("\n❌ Error: Please enter valid numbers for the bill and group size.")

if __name__ == "__main__":
    bill_splitter()