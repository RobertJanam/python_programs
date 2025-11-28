import random

def play_game():
    number = random.randint(1, 100)
    count = 1
    attempts = 0
    hint_given = False

    while attempts < 4 and count <= 10:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Invalid input!")
                print("Please enter a number between 1 and 100!")
                continue
        except ValueError:
            print("Invalid input!")
            print("Please enter a number between 1 and 100!")
            continue

        attempts += 1

        if guess == number:
            print("You won!")
            print(f"{number} is the correct number.")
            print(f"Total Attempts: {count}")
            return

        else:
            print("Try again!")
            count += 1

    if not hint_given:
        if number <= 50:
            print("Hint: The number is between 1 and 50.")
        else:
            print("Hint: The number is between 51 and 100.")
        hint_given = True

    while attempts < 7:
        try:
            guess = int(input("Guess again: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess == number:
            print("You won!")
            print(f"{number} is the correct number.")
            print(f"Total Attempts: {count}")
            return

        else:
            print("Try again!")
            count += 1

    if attempts == 7:

        range_start = (number // 10) * 10
        range_end = range_start + 10
        print(f"Hint: The number is between {range_start} and {range_end}.")

    while attempts < 10:
        try:
            guess = int(input("Guess again: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess == number:
            print("You won!")
            print(f"{number} is the correct number.")
            print(f" Total Attempts: {count}")
            return

        else:
            print("Try again!")
            count += 1

    if attempts == 10:
        print(f"You failed! The correct number was {number}.")
        print(f"Attempts: {count}")
        return

while True:
    play_game()
    if input("Play again? (y/n): ").lower() != 'y':
        break