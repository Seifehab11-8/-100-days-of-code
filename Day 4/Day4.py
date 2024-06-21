rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Welcome rock paper scissor game
import random
print("Welcome to Rock Paper Scissors!")
human_choice = int(input("To choose Rock:0 | Paper:1 | Scissors:2\nchoose a number: "))
list_of_graphics = [rock, paper, scissors] #list of graphical outcomes
list_of_choice = ["Rock", "Paper", "Scissors"]
computer_choice = random.randint(0,2) #random number generation
if(human_choice < 3 and human_choice >= 0): # making sure the user inputs are correct
    print(f"human_choice: {list_of_choice[human_choice]}\n" + list_of_graphics[human_choice])
    print(f"computer_choice: {list_of_choice[computer_choice]}\n" + list_of_graphics[computer_choice])

#possible actions a there outcomes
if(human_choice == computer_choice):
    print("The match is a DRAW")
elif(human_choice == 0 and computer_choice == 1):
    print("Computer won the match")
elif(human_choice == 1 and computer_choice == 0):
    print("You won the match")
elif(human_choice == 1 and computer_choice == 2):
    print("Computer won the match")
elif(human_choice == 2 and computer_choice == 1):
    print("You won the match")
elif(human_choice == 2 and computer_choice == 0):
    print("Computer won the match")
elif(human_choice == 0 and computer_choice == 2):
    print("You won the match")
else:
    print("You lost!, invalid input")



