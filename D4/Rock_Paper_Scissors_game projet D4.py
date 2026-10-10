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
user = int(input('What do you choose? Type 0 for "Rock", 1 for "Paper" or 2 for "Scissors".\n'))
user_list = [rock, paper, scissors]
if user == 0 or user == 1 or user == 2:
    print("You chose:")
    print(user_list[user])
    print("Computer chose:")
    comp = [rock, paper, scissors]
    game_index = random.randint(0, 2)
    comp_choice = comp[game_index]
    print(comp_choice)
    if user == game_index:
        print("It's a Draw!")
    elif (user == 2 and game_index == 1
          or user == 0 and game_index == 2 or user == 1 and game_index == 0) :
        print("You Win!")
    else:
        print("You Lose!")
else:
    print("Please enter a valid option")