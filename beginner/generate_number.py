import random

# ask user to choose generate or close program
print("Choose generate to give random value from 0 to 100")
print("Choose exit to quit")

while True:
    print("\ngenerate = g")
    print("exit = e")
    choice_of_user = input("> ").lower()
    # if generate, randomly give a number from 0 to 100
    if choice_of_user == 'g':
        
        #Ask user how many times they would like to generate a number
        print("Enter number of times you would like to generate a number"
              " between 0 and 100."
              "\nMaximum limit is 10.")
        limit = 10
        count = 0
        number_of_generations = int(input("> "))
        # Only executed when number of generations is less than or equal to the limit given
        if number_of_generations <= limit:
            print("Type (s) start generating values or (r) to return")
            # Loop occurs so long as count is still less than the number of generations
            while count < number_of_generations:
                userTypes = input("s/r > ").lower()
                if userTypes == 's':
                    number = random.randint(0, 100)
                    print(f"Number: {number}")
                    count += 1 # count = count + 1, adds one to count until the condition is no longer met
                    if count >= number_of_generations:
                        print("Would you like to continue?(y/n)")
                        try_again = input("> ")
                        if try_again == 'y':
                            continue
                        elif try_again == 'n':
                            print("Exiting...")
                            quit()# breaks the entire program
                        else:
                            print("Invalid")
                elif userTypes == 'r':
                    print("Returning...")# goes back to the start of the program 
                    break
                else:
                    print("Invalid")
                    continue
        else:
            print("Number has exceeded the limit. "
                  "Try entering a number between 1 and 10")

    elif choice_of_user == 'e':
        print("Exiting...")
        exit()# same as quit()
    else:
        print("Invalid")