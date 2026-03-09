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

images = [rock, paper, scissors]
computerChoice = random.randint(0, len(images) - 1)
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(images[userChoice])
print("Computer chose: ")
print(images[computerChoice])
if userChoice == computerChoice:
    print("It is a draw!")
elif userChoice == 0:
    if computerChoice == 1:
        print("You Loose!")
    elif computerChoice == 2:
        print("You Win!")
elif userChoice == 1:
    if computerChoice == 0:
        print("You win!")
    elif computerChoice == 2:
        print("You Loose!")
elif userChoice == 2:
    if computerChoice == 0:
        print("You Loose!")
    elif computerChoice == 1:
        print("You Win!")
else:
    print("Choose a valid option!")
