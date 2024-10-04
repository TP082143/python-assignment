#main function of the program
def main():
    print("-------------------------------------------------")
    print("Welcome to Delicious Restaurant Management System")
    print("-------------------------------------------------")
    login()

#login attempts function
def login():
    attempts = 0
    while attempts < 3:
        user_name = input("Enter your username or email: ")
        pass_word = input("Enter your password: ")
        value = validate_login(user_name, pass_word)
        if value is not None:
            if value[1] == "admin":
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Hello, {value[0]}. This is your Administration Portal.")
                admin_menu(value[0])
                break
            elif value[1] == "manager":
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Hello, {value[0]}. This is your Manager Portal.")
                break
            elif value[1] == "chef":
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Hello, {value[0]}. This is your Chef Portal.")
                break
            elif value[1] == "customer":
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Hello, {value[0]}. This is your Customer Portal.")
                break
        else:
            left = 2 - attempts
            attempts += 1
            if attempts < 3:
                print(f"Invalid Credentials. {left} attempts left.")

        if attempts == 3:
            print("Maximum login attempts exceeded! Thank you.")


# --- login justification function starts ---
def validate_login(user_name, pass_word):
    lst = []
    with open("user.txt", "r") as file:
        for line in file:
            lst = line.strip().split(",")
            if (lst[1] == user_name or lst[2] == user_name) and lst[3] == pass_word:
                return lst[0], lst[4]
    return None
# --- login justification function ends ---

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
                print("\n")
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
        try:
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
        except ValueError:
            print("Invalid input. Please try again!")

def add_staff():
    print("add staff")
def edit_staff():
    print()
def delete_staff():
    print()

# --- View Sales Section Starts ---
def view_sales():
    while True:
        try:
            print("\nChoice to view sales report:")
            print("1. Specific Month Report")
            print("2. Full Report")
            print("3. Back to Admin Menu\n")
            selection = int(input("Enter your choice: "))
            match selection:
                case 1:
                    month = input("\nEnter the month: ")
                    month_report(month)
                case 2:
                    print("\nLoading full sales report:")
                case 3:
                    print("Taking Back...")
                    break
                case _:
                    print("Invalid input! Try again.")
        except ValueError:
            print("Invalid input! Try again.")

def month_report(month):
    report = []
    total = 0
    print(f"\n{month.title()} Sales Report:")
    print("______________________________________")
    with open("sales_report.txt", "r") as file:
        for line in file:
            report = line.strip().split(",")
            if report[0] == month.title():
                print(f"Customer ID - {report[1]} || Customer name - {report[2]} || Cuisine Type - {report[3]} || Dish - {report[4]} || Price - RM{report[5]} ")
                total = total + float(report[5])
    while True:
        yorn = input("\nDo you want to see the total sale? Y/N: ").strip().upper()
        if yorn == 'Y':
            print(f"Total sales = RM{total}")
            break
        elif yorn == 'N':
            break
        else:
            print("Wrong Input. Please try again!")


# --- View Sales Section Ends ---

# --- View Feedback Section Starts ---
def view_feedback():
    customer_feedback = []
    i = 1
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    with open("customer_feedback.txt", "r") as file:
        for  line in file:
            customer_feedback = line.strip().split(",")
            print(f"{i}. CUSTOMER_ID - {customer_feedback[0]} | CUSTOMER_NAME - {customer_feedback[1]} | COMMENT - {customer_feedback[2]} | RATING - {customer_feedback[3]}")
            i += 1
# --- View Feedback Section Ends ---

# --- Update Profile Section Starts ---
def update_profile(name):
    print("\n~~~~~~ Update your profile ~~~~~~")
    print("1. Name")
    print("2. Username")
    print("3. Email")
    print("4. Password")
    print("5. Back to Admin Menu")
    while True:
        try:
            modify_num = int(input("Select option to modify name/username/email/password: "))
            container = modification_for_update(name, modify_num)
            if container == 1:
                break
            else:
                continue
        except ValueError:
            print("Invalid input! Try again.")


def modification_for_update(pre_name, modify_num):
    staff = []
    info = []
    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if pre_name == info[0]:
                if modify_num == 1:
                    info[0] = input("Enter new name: ")
                elif modify_num == 2:
                    info[1] = input("Enter new username: ")
                elif modify_num == 3:
                    info[2] = input("Enter new email: ")
                elif modify_num == 4:
                    info[3] = input("Enter new password: ")
                elif modify_num == 5:
                    print("Loading...")
                    return 1
                else:
                    print("Invalid input! Try again")
                    return 0
            staff.append([info[0], info[1], info[2], info[3], info[4]])
            print(staff)
    with open("user.txt", "w") as file:
        for line in staff:
            print(line)
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")
    print("Successfully updated!\n")
    return 1
# --- Update Profile Section Ends ---


main()
