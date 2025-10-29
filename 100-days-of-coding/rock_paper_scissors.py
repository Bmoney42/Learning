import random

rock = '''
        _______
    ---'   ____)
          (_____)0
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

art  = [rock, paper, scissors]
user_input = int(input("Enter your choice:  0 for rock, 1 for paper, 2 for scissors: \n Enter Your Choice: "))

print(art[user_input])



choices = [0,1, 2]
computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}.")
print(art[computer_choice])

if user_input >= 3 or user_input < 0:
    print("You Typed an invalid number,  You lose!")

elif computer_choice == 0 and user_input == 2:
    print("You Lose")
elif user_input == 0 and computer_choice == 2:
    print("You Win!!")

elif computer_choice  > user_input:
    print("You Lose")

elif user_input == computer_choice:
    print("it's a tie!!")


elif user_input > computer_choice:
    print("you win")




