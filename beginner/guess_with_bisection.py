print("\nThink of an integer between 1 and 128")
print("Use (yes/no) to answer the questions\nI have only 6 attempts to guess the number\n")
a = 0
b = 128
t = 1
while True:
    m = (a+b)/ 2
    print("\nI guessed the number", m)    
    ask_user1 = input("Is {0} correct?: ".format(m))
    if ask_user1 == "Yes".lower():
        print(f"The number you thought of is {m}\nAttempts: {t}")
        quit()
    elif ask_user1 == 'No'.lower():
        if t >= 6:
            print("\nSorry i couldn't guess your number after 6 attempts")
            break
        elif t < 6:
            ask_user2 = input("Is {0} larger?: ".format(m))
            if ask_user2.lower() == "yes":
                b = m
                t += 1
                continue
            elif ask_user2.lower() == "no":
                a = m
                t += 1
                continue
            else:
                print("Invalid")
    else:
        print("Invalid")