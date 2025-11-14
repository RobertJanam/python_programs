def ask_user():
    while True:
        ask = input("Open calculator?(y/n): ").lower()
        if ask == 'y':
            error_handling()
        elif ask == 'n':
            print("---")
            break
        else:
            print("Invalid input!")

def math(num1, num2):
    op = input("operator: ")
    if op == '+':
        add = num1 + num2
        print(f"Answer = {add:.2f}")
    elif op == '-':
        sub = num1 - num2
        print(f"Answer = {sub:.2f}")
    elif op == '*':
        multi = num1 * num2
        print(f"Answer = {multi:.2f}")
    elif op == '/':
        div = num1 / num2
        print(f"Answer = {div:.2f}")
    else:
        print("Invalid input!")
    print("OFF")

def error_handling():
    while True:
        try:
            print("ON")
            num1 = input("First number: ")
            num1 = float(num1)
            num2 = input("Second number: ")
            num2 = float(num2)
            math(num1, num2)
            break
        except ValueError:
            print("Invalid input!")
        except ZeroDivisionError:
            print("Cannot divide by zero!")

ask_user()