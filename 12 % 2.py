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
---'    ____)____
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
game_images = [rock, paper, scissors]
rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"  ))
print(game_images[rps])
pc = random.randint(0, 2)
print("Computer choose :")
print(game_images[pc])
if rps >= 3 or rps < 0:
    print("You typed an invalid number. You lose!")    
elif rps == 0 and pc == 2:
    print("You win!")
elif pc == 0 and rps == 2:
    print("You lose!")
elif pc > rps:
    print("You lose!")
elif rps > pc:
    print("You win!")
elif pc == rps:
    print("Its a draw!")
elif rps >= 3 or rps < 0:
    print("You typed an invalid number. You lose!")    