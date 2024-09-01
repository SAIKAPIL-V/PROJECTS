import random
user_choice=int(input("Enter your choice, type 0 for Rock , 1 for paper, 2 for scissors\t"))
if user_choice>=3 or user_choice<0:
    print("You Entered invalid number , You lose.")
else:
    computer_choice=random.randint(0,2)
    print("Computer Choice :",computer_choice)
    if computer_choice==user_choice:
        print("It's a tie")
    elif computer_choice==0 and user_choice==2:
        print("You Lose. better luck next time")
    elif user_choice==0 and computer_choice==2:
        print("You Win. Congratulations!")
    elif computer_choice> user_choice:
        print("You Lose. better luck next time")
    elif user_choice>computer_choice:
        print("You Win. Congratulations!")

