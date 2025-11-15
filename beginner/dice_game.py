# start
import random

total_roll_count = 0

while True:
    choice = input("Roll a dice? (y/n): ").lower()
    if choice == "y":
        total_play_list = []
        play_count = 0
        roll_dice = 0
        dice_count = 0
        
        try:
            dice_limit = int(input("How many times do you want to roll?: "))
            while dice_count < dice_limit:
                play = input("roll? (y/n): ").lower()
                if play == 'y':
                    die1 = random.randint(1, 6) 
                    print(f"({die1})")
                    dice_count += 1
                    roll_dice += 1
                    total_roll_count += 1
                    print(f"You have rolled the dice for - {roll_dice} - time(s) during the session")
                    if dice_count == dice_limit:
                        play_count += 1
                        total_play_list.append(play_count)
                elif play == 'n':
                    print("back\n")
                    break
                else:
                    print("invalid choice")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
    elif choice == "n":
        print(f"Total rolls: {total_roll_count}")
        output = 0
        for count in total_play_list:
            output += count
            print(f"Total plays: {count}")
        print("thanks for playing")
        break
    else:
        print("Invalid choice")   
# end