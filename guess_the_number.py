import random


print("""██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║""")


easy_level_attempts=10
hard_level_attempts=5
def set_difficult(level_chosen):
  if level_chosen=="easy":
    return easy_level_attempts
  elif level_chosen=="hard":
    return hard_level_attempts
  else:
    return
  

def check_answer(number_guessed,answer,attempts):
  if number_guessed<answer:
    print("Your guess is too low")
    return attempts-1
  elif number_guessed>answer:
    print("Your guess is too high")
    return attempts-1
  else:
    print(f"Your Guess is right ,The answer was {answer}")
    print(f"\nleft attempts are :{attempts-1}")

def game():
  print("let me think of a number between 1 to 50. ")
  answer=random.randint(1,50)
  level=input("Choose level of dufficulty , Type 'easy' or 'hard' :").lower()
  attempts=set_difficult(level)
  if attempts!= easy_level_attempts and attempts!=hard_level_attempts:
    print("...play again !!  Invalid input , Please choose 'easy' or 'hard' ")
    return
  number_guessed=0
  while number_guessed!=answer:
    print(f"You have {attempts} remaining to guess the number .")
    number_guessed=int(input ("Guess a number:"))
    attempts=check_answer(number_guessed,answer,attempts)
    if attempts==0:
      print("you are out of guesses .. You lose!")
      return 
    elif number_guessed!=answer:
      print("Guess again")
    



game()
