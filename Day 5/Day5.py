#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#defining the password list
password = []

for i in range(0, nr_letters):
    password.append(letters[random.randint(0, len(letters)-1)])
    # alternative using random.choice to choose from the list itself (easier and more covinient)

for j in range(nr_symbols):
    password.append(symbols[random.randint(0, len(symbols)-1)])

for k in range(nr_numbers):
    password.append(numbers[random.randint(0, len(numbers)-1)])

 # shuffle function randomly changes the position of all elements of a list
 # functions that cause a change to a list return none but change the input list

random.shuffle(password) # that is why we don't need a recieve variable

password = "".join(password) # convert list to string
#we could use a for loop instead of join function
print("Your New Password is: " + password)

