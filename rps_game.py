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

import random
rps = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if  2 >= player_choice >= 0:
    print(rps[player_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n"
          f"{rps[computer_choice]} ")
    if player_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif player_choice == 2 and computer_choice == 0:
        print("You Lose!")
    elif player_choice == computer_choice:
        print("It's a Draw!")
    elif player_choice < computer_choice:
        print("You Lose!")
    elif player_choice > computer_choice:
        print("You Win!")
else:
    print("You typed an invalid number, Game Over!!")
