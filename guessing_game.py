import random

random_number = random.randomint(1,10) # numbers 1 - 10

guess = None

while guess != random_number:
    guess = input("Pick a numbner from 1 to 10:")
    guess = int(guess)
    
    print("Too low!")
else:
    print("Too high!")

print(random_number)
# handle user guesses
#   if they guess correct,  tell them they won
#       otherwise thell them if they are too high or too low

#BONUS - let player play again if they want!

