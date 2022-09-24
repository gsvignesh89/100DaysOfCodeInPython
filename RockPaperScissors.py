import random
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

game_images  = [rock, paper, scissors]
#Write your code below this line 👇
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input >= 3 or user_input < 0:
  print("You type a invalid number, You lose")
else:
  print(game_images[user_input])
  
  print("Computer Chose:")
  
  computer_choice = random.randint(0, 2)
  print(game_images[computer_choice])
  
  
  if user_input == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice > user_input:
    print("You lose")
  elif user_input == 2 and computer_choice == 0:
    print("You lose")
  elif user_input > computer_choice:
    print("You win!")
  else:
    print("It's a draw")
