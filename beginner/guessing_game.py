# Guess a number between 1 and 10
# Validations are minimal
import random

print("Guess a number between 1 and 10")
print("You have three attempts.")
correct_guess = random.randint(1,10)
guess_count = 0
guess_limit = 3
# While loop is used to execute a block of code so long as the condition is true.
while guess_count < guess_limit:
    try:
        guess = int(input('guess: '))
        guess_count += 1
        if guess == correct_guess:
            print('You have won!')
            break
    except ValueError:
        print("Invalid input.")
            
else:
    print('sorry you failed. the correct number is ', correct_guess)