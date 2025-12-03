"""Technically similar to the playlist code."""

def main ():
    print("----Password saver----\n")
    file_name = 'Password.txt'
    password_dict = {}
    while True:
        name_of_service = input("Enter name of the service\nor type (stop) to exit: ")
        if name_of_service == 'stop'.lower():
            break
        password = input("Enter the the password: ").strip()
        
        password_dict[name_of_service] = password
        print("Saved successfully ✔")

    print("Status: Active")
    print("Update: Successful")
    print("Runtime: Clear")
    write_to_file(file_name, password_dict)

def write_to_file(file_name, password_dict):
    with open(file_name, 'a') as file:
        for name_of_service, password in password_dict.items():
            file.write(f"{name_of_service} - {password}\n")

        print("Saved successfully to file.txt 🖍")

main()