#greeting
print("Welcome to the tip calculator!")
#recieving total bill
total_Bill = float(input("What is your total bill? $"))
#calculate the tip amount
total_tip = float(input("How much tip do you like to give (10% , 12%, 15%) $")) * (total_Bill/100)
numOfPeople = int(input("How many people to split the bill? $"))

total = total_tip + total_Bill
total_per_person = total/numOfPeople

total_per_person = round(total_per_person ,2) # rounds to 2 decimal places
# f-string to make automatic casting to string type
print(f"Each person should pay: ${total_per_person}")
