#mean
def user_input():
    input_list = int(input("Enter number of elements: "))
    data = []
    for i in range(0, input_list):
        element = int(input("> "))
        data.append(element)
    return data
def calculate_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    data = user_input()
    print(f"Mean: {calculate_mean(data)}")