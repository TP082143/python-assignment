#main function of the program
def main():
    print("-------------------------------------------------")
    print("Welcome to Delicious Restaurant Management System")
    print("-------------------------------------------------")
    login()

#login attempts function
def login():
    attempts = 0
    while (attempts < 3):
        user_name = input("Enter your username or email: ")
        pass_word = input("Enter your password: ")
        value = validate_login(user_name, pass_word)
        if value is not None:
            if value[1] == "admin":
                print(f"\nHello, {value[0]}. This is your Administration Portal.")
                admin_menu(value[0])
                break
            elif value[1] == "manager":
                print(f"\nHello, {value[0]}. This is your Manager Portal.")
                break
            elif value[1] == "chef":
                print(f"\nHello, {value[0]}. This is your Chef Portal.")
                break
            elif value[1] == "customer":
                print(f"\nHello, {value[0]}. This is your Customer Portal.")
                break
        else:
            left = 2 - attempts
            attempts += 1
            if (attempts < 3):
                print(f"Invalid Credentials. {left} attempts left.")

        if (attempts == 3):
            print("Maximum login attempts exceeded! Thank you.")


#login justification function
def validate_login(user_name, pass_word):
    with open("user.txt", "r") as file:
        for line in file:
            name, username, email, password, role = line.strip().split(",")
            if (username == user_name or email == user_name) and password == pass_word:
                return name, role
    return None

def admin_menu(name):
    while True:
        print("\n~~~~~~Admin Menu~~~~~~")
        print("1. Manage Staff")
        print("2. View Sales Report")
        print("3. View Feedback")
        print("4. Update Profile")
        print("5. Logout")
        selection = input("Select an option: ")

        match selection:
            case "1":
                manage_staff()
            case "2":
                view_sales()
            case "3":
                view_feedback()
            case "4":
                update_profile(name)
            case "5":
                print("Thank you. Have a good day!")
                break
            case _:
                print("Invalid Input. Please try again!")

def manage_staff():
    while True:
        print("\n~~~~~~ Manage Staff ~~~~~~")
        print("1. Add Staff")
        print("2. Edit Staff")
        print("3. Delete Staff")
        print("4. Back to Admin Menu")
        selection = input("Select an option: ")

        match selection:
            case "1":
                add_staff()
            case "2":
                edit_staff()
            case "3":
                delete_staff()
            case "4":
                break
            case _:
                print("Invalid input. Please try again!")


def view_sales():
    print()
def view_feedback():
    print()
def update_profile(name):
    print("\n~~~~~~ Update your profile ~~~~~~")
    print("1. Name")
    print("2. Username")
    print("3. Email")
    print("4. Password")
    while True:
        modify_num = int(input("Select option to modify name/username/email/password: "))
        container = modification_for_update(name, modify_num)
        if container == 1:
            break
        else:
            continue


def modification_for_update(pre_name, modify_num):
    staff = []
    with open("user.txt", "r") as file:
        for line in file:
            name, username, email, password, role = line.strip().split(",")
            if pre_name == name:
                if modify_num == 1:
                    name = input("Enter new name: ")
                elif modify_num == 2:
                    username = input("Enter new username: ")
                elif modify_num == 3:
                    email = input("Enter new email: ")
                elif modify_num == 4:
                    password = input("Enter new password: ")
                else:
                    print("Invalid input! Try again")
                    return 0
            staff.append([name, username, email, password, role])
    with open("user.txt", "w") as file:
        for line in staff:
            print(staff)
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")
    print("Successfully updated!\n")
    return 1

def add_staff():
    print("add staff")
def edit_staff():
    print()
def delete_staff():
    print()
main()