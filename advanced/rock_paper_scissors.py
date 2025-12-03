"""Wrote this as a first big project as beginners. I was trying to
see how goofy I could make the game🙂"""

import random

emoji = {
    'r': 'rock 🧱',
    'p': 'paper 📃',
    's': 'scissors ✂'
}

choices = ('r', 'p', 's')

def play_game(difficulty_level):
    while True:
        # If difficulty level is hard
        if difficulty_level == 'hard':
            print("\nYou chose a hard level by yourself")
            print("I will show no mercy😈.\n")
            guess = 0
            guess_limit = 5
            while guess < guess_limit:
                user_choice = input('Rock, Paper, Scissors (r,p,s): ').lower()
                if user_choice not in choices:
                    print('Invalid choice')
                    print("Did you even read the instructions?😂. Try again.\n")
                    continue

                if user_choice == 'p':
                    print("You chose paper 📃")
                    print('Computer chose scissors ✂\n')
                    print(f"You lose!")
                    print("You should just stop playing. You are not even good at guessing😂.\n I knew you were going for paper📃\n")
                elif user_choice == 'r':
                    print("You chose rock 🧱")
                    print('Computer chose paper 📃\n')
                    print(f"You lose!")
                    print("You should just stop playing. You are not even good at guessing😂.\n I knew you were going for rock🧱\n")
                elif user_choice == 's':
                    print("You chose scissors ✂")
                    print('Computer chose 🧱\n')
                    print(f"You lose!")
                    print("You should just stop playing. You are not even good at guessing😂.\n I knew you were going for scissors ✂\n")
                
                guess += 1

                if guess < guess_limit:
                    play_again = input("Want to play again? (y/n): ").lower()
                    if play_again == 'y':
                        continue
                    elif play_again == 'n':
                        return
                    else:
                        print("Invalid choice!")
                        continue

            guess = 0
            guess_limit = 4
            while guess < guess_limit:
                print("Aren't you tired of loosing?😂")
                print("Ok, Let me make it a little easy. Be careful! it's still a hard level.🦾\n")
                user_choice = input('Rock, Paper, Scissors (r,p,s): ').lower()
                if user_choice not in choices:
                    print('Invalid choice')
                    print("Did you even read the instructions?😂. Try again.\n")
                    continue

                computer_choice = random.choice(choices)
                print(f'You chose {emoji[user_choice]}')
                print(f'Computer chose {emoji[computer_choice]}\n')

                if user_choice == computer_choice:
                    print("Draw!")
                    print("You are getting better. but not good enough to beat me😅\n")
                elif (
                    (user_choice == 'r' and computer_choice == 's') or
                    (user_choice == 'p' and computer_choice == 'r') or
                    (user_choice == 's' and computer_choice == 'p')
                ):
                    print('You Win!🥳')
                    print("Finally you managed to win. Good for you👍.But don't get too excited. \nI will get you next time😎\n")
                else:
                    print("You lose")
                    print("It is becoming a norm for you to lose🤣.I win again.Try better next time👍\n")

                guess += 1

                if guess < guess_limit:
                    play_again = input("Want to play again? (y/n): ").lower()
                    if play_again == 'y':
                        continue
                    elif play_again == 'n':
                        return
                    else:
                        print("Invalid choice!")
                        continue

            continue  # Jump back to the first while loop

        # If difficulty level is medium
        elif difficulty_level == 'medium':
            print("\nYou chose a medium level")
            print("This one should be interesting.😎 Let's see who wins!🦾\n")
            user_choice = input('Rock, Paper, Scissors (r,p,s): ').lower()
            if user_choice not in choices:
                print('Invalid choice')
                print("Did you even read the instructions?😂. Try again.\n")
                continue

            computer_choice = random.choice(choices)
            print(f'You chose {emoji[user_choice]}')
            print(f'Computer chose {emoji[computer_choice]}\n')

            if user_choice == computer_choice:
                print("Draw!")
                print("You are good. But are you good enough to beat me😎? \nRemember we are equals in this level.\n")
            elif (
                (user_choice == 'r' and computer_choice == 's') or
                (user_choice == 'p' and computer_choice == 'r') or
                (user_choice == 's' and computer_choice == 'p')
            ):
                print('You Win!')
                print("Congratulations!👏 You won😀. You managed to beat me.\n")
            else:
                print("You lose")
                print("We are equals in this level but you still managed to lose🥱\n")

            play_again = input("Want to play again? (y/n): ").lower()
            if play_again == 'y':
                continue
            elif play_again == 'n':
                return
            else:
                print("Invalid choice!")
                continue

        # If difficulty level is easy
        elif difficulty_level == 'easy':
            print("\nYou chose an easy level for yourself")
            print("Are you a coward? Just kidding!😅")
            print("This is a piece of cake. I will go easy on you. Let's see if you can win!\n")
            guess = 0
            guess_limit = 4
            while guess < guess_limit:
                user_choice = input('Rock, Paper, Scissors (r,p,s): ').lower()
                if user_choice not in choices:
                    print('Invalid choice')
                    print("Did you even read the instructions?😂. Try again.\n")
                    continue

                if user_choice == 'p':
                    print("You chose paper 📃")
                    print('Computer chose rock 🧱\n')
                    print(f"You win!")
                    print("No fair, you knew i would I would choose rock🧱.\nI will get you next time😣\n")
                elif user_choice == 'r':
                    print("You chose rock 🧱")
                    print('Computer chose scissors ✂\n')
                    print(f"You win!")
                    print("No fair, you knew i would I would choose scissors✂ .\nI will get you next time😣\n")
                elif user_choice == 's':
                    print("You chose scissors ✂")
                    print('Computer chose paper 📃\n')
                    print(f"You win!")
                    print("No fair, you knew i would I would choose paper📃.\nI will get you next time😣\n")
                guess += 1
                
                
                if guess < guess_limit:
                    play_again = input("Want to play again? (y/n): ").lower()
                    if play_again == 'y':
                        continue
                    elif play_again == 'n':
                        return
                    else:
                        print("Invalid choice!")
                        continue

            guess = 0
            guess_limit = 4
            while guess < guess_limit:
                print("You are winning a lot. I cannot let you outshine me. Let's see who wins this time!😈\n")
                user_choice = input('Rock, Paper, Scissors (r,p,s): ').lower()
                if user_choice not in choices:
                    print('Invalid choice')
                    print("Did you even read the instructions?😂. Try again.\n")
                    continue

                computer_choice = random.choice(choices)
                print(f'You chose {emoji[user_choice]}')
                print(f'Computer chose {emoji[computer_choice]}\n')

                if user_choice == computer_choice:
                    print("Draw!")
                    print("I've managed to draw with you.\n")
                elif (
                    (user_choice == 'r' and computer_choice == 's') or
                    (user_choice == 'p' and computer_choice == 'r') or
                    (user_choice == 's' and computer_choice == 'p')
                ):
                    print('You Win!')
                    print("You were just lucky😪\n")
                else:
                    print("You lose")
                    print("Haha!🤣. I win. Told you I will not let you win this time.😎\n")

                if guess < guess_limit:
                    play_again = input("Want to play again? (y/n): ").lower()
                    if play_again == 'y':
                        continue
                    elif play_again == 'n':
                        return
                    else:
                        print("Invalid choice!")
                        continue
            continue

def difficulty_choice():
    while True:
        print("***You Are Playing a Game of ROCK, PAPER, SCISSORS***")
        print("                       Enjoy                    ")
        print("""Difficulty Level:
1. Easy
2. Medium 
3. Hard""")

        try:
            level = int(input("Choose difficulty (1-3): "))
            if level == 1:
                play_game('easy')
            elif level == 2:
                play_game('medium')
            elif level == 3:
                play_game('hard')
            else:
                print('Invalid choice. Please enter 1, 2, or 3.')
                continue

            another_game = input("Do you want to choose a different difficulty? (y/n): ").lower()
            if another_game != 'y':
                quit()

        except ValueError:
            print('Please enter a valid number (1-3).')

if __name__ == "__main__":
    difficulty_choice()