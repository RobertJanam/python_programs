# square
def square_pattern():
    for i in range(3):
        for j in range(6):
            print("*", end="")
        print()
        
# right-angle triangle
def right_triangle_pattern():
    number = [1, 2, 3, 4, 5]
    for i in number:
        print("*" * i)

    for j in range(1, 6):
            print("*" * j)
        
def reverse_right_triangle_pattern():
    number = [1, 2, 3, 4, 5]
    reverse_number = sorted(number, reverse=True)
    for i in reverse_number:
        print("*" * i)

def triangle_pattern():
    number = [1, 2, 3, 4, 5]
    for i in number:
        print(" " * (number[-1] - i) + "* " * i)
        
def triangle_pattern_range():
    for i in range(1, 6):
        print(" " * (6 - i), "* " * i)

def reverse_triangle():
    rows = 5
    for i in range(rows, 0, -1):
        print(" " * (rows - i), end="")
        print("* " * i)
        
def reverse_triangle_2():
    number = [1, 2, 3, 4, 5]
    reverse_number = sorted(number, reverse=True)
    for i in reverse_number:
        print(" " * (number[-1] - i), end="")
        print("* " * i)
        
print(square_pattern())
print(right_triangle_pattern())
print(reverse_right_triangle_pattern())
print(triangle_pattern())
print(triangle_pattern_range())
print(reverse_triangle())
print(reverse_triangle_2())