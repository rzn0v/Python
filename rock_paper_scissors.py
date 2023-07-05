#ascii arts for representation of handsignals
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

import random #random module

choices=[rock, paper, scissors]

random_number= random.randint(0,2)

user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

print(choices[user])

print("\nComputer chose:\n")

print(choices[random_number])

#rock(0) beats scissors(2)
#scissors(2) beats paper(1)
#paper(1) beats rock(0)

if user==0 and random_number==2:
  print("You win!")
elif user==1 and random_number==0:
  print("You win!")
elif user==2 and random_number==1:
  print("You win!")
elif user-random_number==0:
  print("It's a draw!")

else:
  print("You lose!")