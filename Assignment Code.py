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
                manager_menu(value[0])
                break
            elif value[1] == "chef":
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Hello, {value[0]}. This is your Chef Portal.")
                # User registration and login system
                while True:
                    print("\n1. Register")
                    print("2. Chef Management Menu")
                    print("3. Logout")

                    choice = input("Select your choice (1-3): ")

                    if choice == '1':
                        registration()
                    elif choice == '2':
                        chef_management_menu(value[0], user_name)  # Proceed to main management system if login is successful
                    elif choice == '3':
                        print("Exiting program...")
                        break
                    else:
                        print("Invalid choice! Please pick between (1-3).")
                break
            elif value[1] == "customer":
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Hello, {value[0]}. This is your Customer Portal.")
                customer_menu(value[0], user_name)
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

# --- admin menu starts ---
def admin_menu(name):
    while True:
        print("\n~~~~~~ Admin Menu ~~~~~~")
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
                print("Invalid input. Please try again!")
# --- admin menu ends ---

# --- admin manage staff function starts ---
def manage_staff():
    while True:
        print("\n~~~~~~ Manage Staff ~~~~~~")
        print("1. Add Staff")
        print("2. Edit Staff")
        print("3. Delete Staff")
        print("4. Back to Admin Menu")
        info = []
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

#add staff function
def add_staff():
    while True:
        try:
            print("\nDo you want to add manager or chef?\n1. Manager\n2. Chef\n3. Back")
            selection = int(input("\nSelect your choice: "))
            match selection:
                case 1:
                    add_staff_manager()
                case 2:
                    add_staff_chef()
                case 3:
                    break
                case _:
                    print("Wrong input! Try again.")
        except ValueError:
            print("Wrong input! Try again")

#add manager function
def add_staff_manager():
    print("Enter the details to add manager: ")
    info = []
    i = 0
    while i < 5:
        if i == 0:
            info.append(input("Enter the name: "))
        elif i == 1:
            info.append(input("Enter username: "))
        elif i == 2:
            info.append(input("Enter email address: "))
        elif i == 3:
            info.append(info[1] + "123")
        elif i == 4:
            info.append("manager")
        i += 1
    with open("user.txt", "a") as file:
        file.write(f"{info[0]},{info[1]},{info[2]},{info[3]},{info[4]}\n")
    print("Added Successfully!")

#add chef function
def add_staff_chef():
    print("Enter the details to add chef: ")
    info = []
    i = 0
    while i < 5:
        if i == 0:
            info.append(input("Enter the name: "))
        elif i == 1:
            info.append(input("Enter username: "))
        elif i == 2:
            info.append(input("Enter mail address: "))
        elif i == 3:
            info.append(info[1] + "123")
        elif i == 4:
            info.append("chef")
        i += 1
    with open("user.txt", "a") as file:
        file.write(f"{info[0]},{info[1]},{info[2]},{info[3]},{info[4]}\n")
    print("Added Successfully!")

def staff_list():
    with open("user.txt", "r") as file:
        print("\nManagers: ")
        for line in file:
            info = line.strip().split(",")
            if info[4] == "manager":
                print(f"Name - {info[0]} | Username - {info[1]} | Email - {info[2]}")
    with open("user.txt", "r") as file:
        print("\nChef: ")
        for line in file:
            info = line.strip().split(",")
            if info[4] == "chef":
                print(f"Name - {info[0]} | Username - {info[1]} | Email - {info[2]}")

#edit staff details function
def edit_staff():
    staff_list()
    while True:
        try:
            print("\nEnter the choice to edit:")
            print("1. Manager")
            print("2. Chef")
            print("3. Back")
            selection = int(input("Select your option: "))
            match selection:
                case 1:
                    username = input("Enter the username of the manager: ")
                    role = "manager"
                    container = edit_staff_manager(username, role)
                case 2:
                    username = input("Enter the username of the chef: ")
                    role = "chef"
                    container = edit_staff_chef(username, role)
                case 3:
                    break
                case _:
                    print("Wrong input! Try again.")
        except ValueError:
            print("Wrong input! Try again.")


def edit_staff_manager(username, role):
    value = 0
    data = []
    # Reading the file
    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")

            # Check if the username and role match
            if username == info[1] and role == info[4]:
                value = 1
                while True:  # Loop to keep asking until the correct option is provided
                    print("\nWhat would you like to edit?")
                    print("1. Name")
                    print("2. Username")
                    print("3. Email")
                    print("4. Password")
                    print("5. Back")

                    try:
                        selection = int(input("Choose the option you want to edit: "))

                        match selection:
                            case 1:
                                info[0] = input("\nEnter the new name: ")
                                break
                            case 2:
                                info[1] = input("\nEnter the new username: ")
                                break
                            case 3:
                                info[2] = input("\nEnter the new email: ")
                                break
                            case 4:
                                info[3] = input("\nEnter the new password: ")
                                break
                            case 5:
                                print("Back to menu\n")
                                return 0 # Exit function if the user chooses to go back
                            case _:
                                print("Invalid selection! Please choose a valid option.")
                    except ValueError:
                        print("Invalid input! Please choose a valid option.")

            # Append updated info or unmodified line to data list
            data.append(info)

    # Writing the updated data back to the file
    with open("user.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")

    # Check if editing was successful
    if value == 1:
        print("Successfully Edited!")
        return 1
    else:
        print("No matching username and role found.")

def edit_staff_chef(username, role):
    value = 0
    data = []

    # Reading the file
    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")

            # Check if the username and role match
            if username == info[1] and role == info[4]:
                value = 1
                while True:  # Loop to keep asking until the correct option is provided
                    print("\nWhat would you like to edit?")
                    print("1. Name")
                    print("2. Username")
                    print("3. Email")
                    print("4. Password")
                    print("5. Back")

                    try:
                        selection = int(input("Choose the option you want to edit: "))

                        match selection:
                            case 1:
                                info[0] = input("\nEnter the new name: ")
                                break
                            case 2:
                                info[1] = input("\nEnter the new username: ")
                                break
                            case 3:
                                info[2] = input("\nEnter the new email: ")
                                break
                            case 4:
                                info[3] = input("\nEnter the new password: ")
                                break
                            case 5:
                                print("Back to menu\n")
                                return 0 # Exit function if the user chooses to go back
                            case _:
                                print("Invalid selection! Please choose a valid option.")
                    except ValueError:
                        print("Invalid input! Please choose a valid option.")

            # Append updated info or unmodified line to data list
            data.append(info)

    # Writing the updated data back to the file
    with open("user.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")

    # Check if editing was successful
    if value == 1:
        print("Successfully Edited!")
        return 1
    else:
        print("No matching username and role found.")

def delete_staff():
    staff_list()
    while True:
        try:
            print("\nStaff Deletion Choice:")
            print("1. Manager")
            print("2. Chef")
            print("3. Back")
            selection = int(input("Enter your option: "))
            if selection == 1:
                role = "manager"
                username = input("\nEnter username of the manager: ")
                email = input("Enter email of the manager: ")
                if delete_staff_role(username, email, role) == 1:
                    print("Successfully Deleted")
            elif selection == 2:
                role = "chef"
                username = input("\nEnter username of the chef: ")
                email = input("Enter email of the chef: ")
                if delete_staff_role(username, email, role) == 1:
                    print("Successfully Deleted")
            elif selection == 3:
                break
            else:
                print("Wrong input! Please try again")
        except ValueError:
            print("Wrong input! Please try again")

def delete_staff_role(username, email, role):
    container = 0
    value = 0
    data = []
    info = []
    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if username == info[1] and email == info[2] and role == info[4]:
                container = 1
                break
    if container == 1:
        with open("user.txt", "r") as file:
            for line in file:
                info = line.strip().split(",")
                if not (username == info[1] and email == info[2] and role == info[4]):
                    value = 1
                    data.append(info)
    else:
        print("No such data found!")
        return 0
    with open("user.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")
    if value == 1:
        return 1

# --- admin manage staff function ends ---

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
                    full_report()
                case 3:
                    print("Taking Back...")
                    break
                case _:
                    print("Invalid input! Try again.")
        except ValueError:
            print("Invalid input! Try again.")

    #specific month sales report function
def month_report(month):
    container = 0
    report = []
    total = 0
    with open("sales_report.txt", "r") as file:
        for line in file:
            report = line.strip().split(",")
            if report[0] == month.title():
                container = 1
    if container == 1:
        print("______________________________________________________________________________________________________________________")
        print(f"{month.title()} Sales Report:")
        with open("sales_report.txt", "r") as file:
            for line in file:
                report = line.strip().split(",")
                if report[0] == month.title():
                    print(
                        f"Customer name - {report[1]} || Cuisine Type - {report[2]} || Dish - {report[3]} || Price - RM{report[4]}")
                    total = total + float(report[4])
        print("______________________________________________________________________________________________________________________")
    else:
        print("Sorry, there is no sales report for this month.")
        return 0
    while True:
        yorn = input("\nDo you want to see the total sale? Y/N: ").strip().upper()
        if yorn == 'Y':
            print(f"Total sales = RM{total}")
            break
        elif yorn == 'N':
            break
        else:
            print("Wrong Input. Please try again!")

    #Full Sales Report Function
def full_report():
    lst = []
    total = 0
    for i in range(1, 13):
        file = open("sales_report.txt", "r")
        file.seek(0)
        month_show = 0
        num = 1
        for line in file:
            lst = line.strip().split(",")
            if int(lst[5]) == i:
                if month_show == 0:
                    print("------------------------------------------------------------------------------------------------------------------------")
                    print(f"                                         ~~~~ {lst[0].upper()} Sales ~~~~                                          ")
                    month_show = 1
                print(f"{num} Customer name - {lst[1]} || Cuisine Type - {lst[2]} || Dish - {lst[3]} || Price - RM{lst[4]}")
                total = total + float(lst[4])
                num += 1
        file.close()

        if i == 12:
            print("------------------------------------------------------------------------------------------------------------------------")
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
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("                                                        ~~~~ Feedbacks ~~~~                                                   ")
    print("------------------------------------------------------------------------------------------------------------------------------")
    with open("customer_feedback.txt", "r") as file:
        for  line in file:
            customer_feedback = line.strip().split(",")
            print(f"{i}. CUSTOMER_NAME - {customer_feedback[0]} | CATEGORY - {customer_feedback[1]} | FOOD - {customer_feedback[2]} | COMMENT - {customer_feedback[3]} | RATING - {customer_feedback[4]}")
            i += 1
    print("------------------------------------------------------------------------------------------------------------------------------")
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
    data = []
    info = []
    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            #name = info[0]
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
            data.append(info)
    with open("user.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")
    print("Successfully updated!\n")
    return 1
# --- Update Profile Section Ends ---

#///////////////////------------------------------- SHAMEEL -------------------------///////////////////////////

def manager_menu(name):
    while True:
        print("\n~~~~~~ Manager Menu ~~~~~~")
        print("1. Manage Customers")
        print("2. Manage Menu Categories and Pricing")
        print("3. View Ingredients List Requested by Chef")
        print("4. Update present month")
        print("5. Update Profile")
        print("6. Logout")
        selection = input("Select an option: ")

        match selection:
            case "1":
                manage_customers()
            case "2":
                manage_menu()
            case "3":
                view_ingredients_list()
            case "4":
                update_month()
            case "5":
                update_manager_profile(name)
            case "6":
                print("Thank you. Have a good day!")
                break
            case _:
                print("Invalid input. Please try again!")
# --- manager menu ends ---

# --- manage customers function starts ---
def manage_customers():
    while True:
        print("\n~~~~~~ Manage Customers ~~~~~~")
        print("1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. Back to Manager Menu")
        selection = input("Select an option: ")

        match selection:
            case "1":
                add_customer()
            case "2":
                edit_customer()
            case "3":
                delete_customer()
            case "4":
                break
            case _:
                print("Invalid input. Please try again!")

# Add customer function
def add_customer():
    print("Enter the details to add customer: ")
    name = input("Enter customer name: ")
    username = input("Enter username: ")
    email = input("Enter email address: ")
    password = username + "123"
    role = "customer"
    with open("user.txt", "a") as file:
        file.write(f"{name},{username},{email},{password},{role}\n")
    print("Customer added successfully!")

# Edit customer function
def edit_customer():
    with open("user.txt", "r") as file:
        print("\nCustomers: ")
        for line in file:
            info = line.strip().split(",")
            if info[4] == "customer":
                print(f"Name - {info[0]} | Username - {info[1]} | Email - {info[2]}")
    username = input("Enter the username of the customer: ")
    data = []
    found = False

    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[1] == username and info[4] == "customer":
                found = True
                print("\nWhat would you like to edit?")
                print("1. Name")
                print("2. Username")
                print("3. Email")
                print("4. Password")
                print("5. Back")

                selection = int(input("Choose the option you want to edit: "))

                match selection:
                    case 1:
                        info[0] = input("\nEnter the new name: ")
                    case 2:
                        info[1] = input("\nEnter the new username: ")
                    case 3:
                        info[2] = input("\nEnter the new email: ")
                    case 4:
                        info[3] = input("\nEnter the new password: ")
                    case 5:
                        print("Back to menu\n")
                        return
                    case _:
                        print("Invalid selection! Please choose a valid option.")

            data.append(info)

    with open("user.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")

    if found:
        print("Customer edited successfully!")
    else:
        print("No matching customer found.")

# Delete customer function
def delete_customer():
    username = input("Enter the username of the customer to delete: ")
    data = []
    found = False

    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[1] == username and info[4] == "customer":
                found = True
            else:
                data.append(info)

    with open("user.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")

    if found:
        print("Customer deleted successfully!")
    else:
        print("No matching customer found.")

# --- manage customers function ends ---

# --- manage menu function starts ---
def manage_menu():
    while True:
        print("\n~~~~~~ Manage Menu Categories and Pricing ~~~~~~")
        print("1. Add Menu Item")
        print("2. Edit Menu Item")
        print("3. Delete Menu Item")
        print("4. Back to Manager Menu")
        selection = input("Select an option: ")

        match selection:
            case "1":
                add_menu_item()
            case "2":
                edit_menu_item()
            case "3":
                delete_menu_item()
            case "4":
                break
            case _:
                print("Invalid input. Please try again!")

# Add menu item function
def add_menu_item():
    print("Enter the details to add menu item: ")
    category = input("Enter category: ")
    item_name = input("Enter item name: ")
    price = float(input("Enter price: "))
    with open("menu.txt", "a") as file:
        file.write(f"{category},{item_name},{price}\n")
    print("Menu item added successfully!")

# Edit menu item function

def menu_book():
    cuisine = ['Bengali', 'Italian', 'Indian', 'Western']
    data = []
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~ Food Menu ~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("----------------------------------------------------------")

    # Store all menu data
    with open("menu.txt", "r") as file:
        lines = [line.strip().split(",") for line in file]

    for i in range(len(cuisine)):
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~ {cuisine[i]} ~~~~~~~~~~~~~~~~~~~~~~~~~~")
        y = 1
        for info in lines:
            if cuisine[i] == info[0].title():
                print(f"{y}. Item: {info[1].title()}, Price: RM{info[2]}")
                y += 1
                data.append(info)
    return data

def edit_menu_item():
    menu_book()
    cat = input("Enter the name of the category: ").title()
    item_name = input("Enter the name of the menu item to edit: ").title()
    data = []
    found = False

    with open("menu.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[1].title() == item_name and info[0].title() == cat:
                found = True
                print("\nWhat would you like to edit?")
                print("1. Category")
                print("2. Item Name")
                print("3. Price")
                print("4. Back")

                selection = int(input("Choose the option you want to edit: "))

                match selection:
                    case 1:
                        info[0] = input("\nEnter the new category: ").upper()
                    case 2:
                        info[1] = input("\nEnter the new item name: ").upper()
                    case 3:
                        info[2] = input("\nEnter the new price: ")
                    case 4:
                        print("Back to menu\n")
                        return
                    case _:
                        print("Invalid selection! Please choose a valid option.")

            data.append(info)

    with open("menu.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]}\n")

    if found:
        print("Menu item edited successfully!")
    else:
        print("No matching menu item found.")

# Delete menu item function
def delete_menu_item():
    menu_book()
    cat = input("Enter the name of the category: ")
    item_name = input("Enter the name of the menu item to delete: ")
    data = []
    found = False

    with open("menu.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[1] == item_name.upper() and info[0] == cat.upper():
                found = True
            else:
                data.append(info)

    with open("menu.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]}\n")

    if found:
        print("Menu item deleted successfully!")
    else:
        print("No matching menu item found.")

# --- manage menu function ends ---

def view_ingredients_list():
    lst = []
    i = 1
    with open("ingredients.txt", "r") as file:
        print("\n~~~~~~~~  The List of Ingredients   ~~~~~~~~")
        for line in file:
            lst = line.strip().split(",")
            print(f"{i}. ID: {lst[0]}, Name: {lst[1]}, Quantity: {lst[2]}")
            i += 1
def update_month():
    m_num = int(input("Enter the month in number: "))
    month = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']
    with open("month.txt", "w") as file:
        file.write(f"{month[m_num-1]},{m_num}")
        print("Successfully added!")

def update_manager_profile(name):
    print("\n~~~~~~ Update your profile ~~~~~~")
    print("1. Name")
    print("2. Username")
    print("3. Email")
    print("4. Password")
    print("5. Back to Admin Menu")
    while True:
        try:
            modify_num = int(input("Select option to modify name/username/email/password: "))
            container = modification(name, modify_num)
            if container == 1:
                break
            else:
                continue
        except ValueError:
            print("Invalid input! Try again.")


def modification(pre_name, modify_num):
    data = []
    info = []
    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            #name = info[0]
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
            data.append(info)
    with open("user.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")
    print("Successfully updated!\n")
    return 1

#///////////////////--------------------------------////////////////////////////////////


# ///////////////////-------------------------------- OMAR --------------------------------//////////////////////


def update_order_status(orders, order_id, dish, new_status):
    update_order = []
    order_pop = False
    for order in orders:
        if int(order[0]) == int(order_id) and order[2].lower() == dish.lower():
            print("\nOK!!")
            order_pop = True
            if new_status.lower() in ["in progress", "completed"]:
                order[4] = new_status
                print(f"Order {order_id} status updated to: {order[4]}")
            else:
                print("Invalid status. Please use 'In Progress' or 'Completed'.")
            update_order.append(order)
        else:
            update_order.append(order)

    if not order_pop:
        print(f"Order {order_id} not found.")

    with open("orders.txt", "w") as file:
        for line in update_order:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")


def view_orders(orders):
    if not orders:
        print("No orders placed yet.")
    else:
        print("Customer Orders:")
        for order in orders:
            print(f"- Order ID: {order[0]}, Customer: {order[1]}, Dish: {order[2]}, Quantity: {order[3]} Status: {order[4]}")


def load_ingredients(filename):
    ingredients = []
    try:
        with open(filename, "r") as file:
            for line in file:
                ingredient_id, name, quantity = line.strip().split(",")
                ingredients.append([int(ingredient_id), name, quantity])
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty inventory.")
    return ingredients


def save_ingredients(filename, ingredients):
    with open(filename, "w") as file:
        for ingredient in ingredients:
            file.write(f"{ingredient[0]},{ingredient[1].title()},{ingredient[2]}\n")


def add_ingredient(ingredients):
    ingredient_id = int(input("Enter ingredient ID: "))
    for ingredient in ingredients:
        if ingredient[0] == ingredient_id:
            print("Ingredient ID already exists. Please choose a different ID.")
            return

    name = input("Enter ingredient name: ")
    quantity = input("Enter ingredient quantity: ")
    ingredients.append([ingredient_id, name, quantity])
    save_ingredients("ingredients.txt", ingredients)
    print("Ingredient added successfully!")


def edit_ingredient(ingredients):
    ingredient_id = int(input("Enter ingredient ID to edit: "))
    for ingredient in ingredients:
        if ingredient[0] == ingredient_id:
            ingredient[1] = input("Enter new ingredient name: ")
            ingredient[2] = input("Enter new ingredient quantity: ")
            save_ingredients("ingredients.txt", ingredients)
            print("Ingredient updated successfully!")
            break
    else:
        print("Ingredient not found!")


def delete_ingredient(ingredients):
    ingredient_id = int(input("Enter ingredient ID to delete: "))
    for ingredient in ingredients:
        if ingredient[0] == ingredient_id:
            ingredients.remove(ingredient)
            save_ingredients("ingredients.txt", ingredients)
            print("Ingredient deleted successfully!")
            break
    else:
        print("Ingredient not found!")


def view_ingredients(ingredients):
    if not ingredients:
        print("Ingredient inventory is empty.")
    else:
        print("Current Ingredients:")
        for ingredient in ingredients:
            print(f"- ID: {ingredient[0]}, Name: {ingredient[1]}, Quantity: {ingredient[2]}")


def registration():
    chef_name = input("Enter your name: ")
    chef_username = input("Enter username: ")
    chef_password = input("Enter password: ")
    chef_email = input("Enter your Email: ")
    with open("user.txt", "r") as file:
        for line in file:
            lst = line.strip().split(",")
            if lst[1] == chef_username:
                print("Username already exists. Please choose a different username.")
                return

    with open("user.txt", "a") as file:
        file.write(f"{chef_name},{chef_username},{chef_email},{chef_password},chef\n")
    print("User registered successfully!\n")


def update_profile_chef(username):
    users = []
    found = False
    with open("user.txt", "r") as file:
        for line in file:
            lst = line.strip().split(",")
            if lst[1] == username:
                found = True
                print("Current profile details:")
                print(f"Username: {lst[1]}, Email: {lst[2]}")
                new_username = input("Enter new username (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                new_password = input("Enter new password (leave blank to keep current): ")

                if new_username:
                    lst[1] = new_username
                if new_email:
                    lst[2] = new_email
                if new_password:
                    lst[3] = new_password
            users.append(",".join(lst))
    if found:
        with open("user.txt", "w") as file:
            for user in users:
                file.write(user + "\n")
        print("Profile updated successfully!")
    else:
        print("User not found!")


def chef_management_menu(name, username):
    ingredients = load_ingredients("ingredients.txt")
    orders = []
    info = []
    with open("orders.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            orders.append(info)
    while True:
        print("\nManagement Menu:")
        print("1. Add Ingredient")
        print("2. Edit Ingredient")
        print("3. Delete Ingredient")
        print("4. View Ingredients")
        print("5. Update Order Status")
        print("6. View Orders")
        print("7. Update Profile")
        print("8. Logout")
        print("9. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_ingredient(ingredients)
        elif choice == "2":
            edit_ingredient(ingredients)
        elif choice == "3":
            delete_ingredient(ingredients)
        elif choice == "4":
            view_ingredients(ingredients)
        elif choice == "5":
            order_id = int(input("Enter order ID: "))
            dish = input("Dish name: ")
            new_status = input("Enter new status (In Progress/Completed): ")
            update_order_status(orders, order_id, dish, new_status)
        elif choice == "6":
            view_orders(orders)
        elif choice == "7":
            update_profile_chef(username)
        elif choice == "8":
            print(f"Goodbye, {name}!")
            return
        elif choice == "9":
            print("Exiting program...")
            exit()
        else:
            print("Invalid choice. Please try again.")



#--------------------------------------------------------------------------------------------/////////////////

#---------------------------------------------------- Ahmed ---------------------------------------------------

# --- Customer Portal Implementation ---

def customer_menu(name, username):
    while True:
        print("\n~~~~~~ Customer Menu ~~~~~~")
        print("1. View & Order Food")
        print("2. View Order Status")
        print("3. Edit or Delete Order")
        print("4. Send Feedback")
        print("5. Update Profile")
        print("6. Logout")
        selection = input("Select an option: ")

        match selection:
            case "1":
                view_and_order_food(name, username)
            case "2":
                view_order_status(username)
            case "3":
                edit_delete(username)
            case "4":
                send_feedback(name)
            case "5":
                update_customer_profile(name, username)
            case "6":
                print("Thank you for visiting Delicious Restaurant! Goodbye!")
                break
            case _:
                print("Invalid input. Please try again!")



# View and Order Food Function
def view_and_order_food(name, username):
    data = menu_book()
    store_1 = []
    store_2 = []
    while True:
        choice = input("\nWould you like to place an order? (Y/N): ").strip().upper()
        if choice == 'Y':
            cate = input("Enter the name of the category: ").strip().title()
            item_name = input("Enter the name of the dish you want to order: ").strip().title()
            quantity = int(input("Enter quantity: "))

            # Search in data instead of re-reading file
            item_found = False
            for info in data:
                if info[0].title() == cate and info[1].title() == item_name:
                    with open("orders.txt", "r") as file:
                        for line in file:
                            store_1 = line.strip().split(",")
                            store_2.append(store_1)
                        last_order = store_2[-1]
                        order_id = int(last_order[0]) + 1
                    place_order(order_id, name, username, cate, item_name, quantity, info[2])
                    item_found = True
                    break

            if not item_found:
                print("Item Not Found!")
        elif choice == 'N':
            break
        else:
            print("Invalid input. Please try again!")


# Place Order Function
def place_order(order_id, name, username, cate, item_name, quantity, price):
    with open("orders.txt", "a") as file:
        file.write(f"{order_id},{username},{cate},{item_name},{quantity},Pending\n")
    final_price = float(price) * quantity
    print(f"\nTotal Price : RM{final_price}")

    # Payment options
    print("How would you like to pay?")
    print("1. By Cash")
    print("2. By TnG")
    print("3. By Card")
    select = input("Select option for payment: ")
    print(f"You selected option {select}. Thank you!")
    print("Order placed successfully!")
    month = []
    with open("month.txt", "r") as file:
        for line in file:
            month = line.strip().split(",")
    # Sales report
    with open("sales_report.txt", "a") as file:
        file.write(f"{month[0]},{name},{cate},{item_name},{final_price},{month[1]}\n")


# View Order Status Function
def view_order_status(username):
    found = False
    with open("orders.txt", "r") as file:
        print("\n~~~~~~ Your Orders ~~~~~~")
        for line in file:
            info = line.strip().split(",")
            if info[1] == username:
                print(f"Order ID: {info[0]}, Item: {info[2]}, Quantity: {info[3]}, Status: {info[4]}")
                found = True
    if not found:
        print("No orders found.")

def edit_delete(username):
    while True:
        try:
            print("1. To edit order")
            print("2. To delete order")
            selection = int(input("Enter your selection: "))
            if selection == 1:
                order_id = input("Enter your order ID: ").strip()
                edit_order(order_id, username)
                break
            elif selection == 2:
                order_id = input("Enter your order ID: ").strip()
                delete_order(order_id, username)
                break
            else:
                print("Invalid Option, try again.")
        except ValueError:
            print("Invalid Option, try again.")

def edit_order(order_id, username):
    info = []
    info_sub = []
    store = []
    container = False
    conti = False
    with open("orders.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if order_id == info[0] and username == info[1]:
                container = True
                info[2] = input("Enter category of food: ")
                info[3] = input("Enter dish name: ")
                with open ("menu.txt", "r") as file_sub:
                    for lines in file_sub:
                        info_sub = lines.strip().split(",")
                        if info[2].upper() == info_sub[0] and info[3].upper() == info_sub[1]:
                            conti = True
                            print(f"The price is RM{info_sub[2]}. Please pay it in cash counter.")
                    if not conti:
                        print("No such menu found!")
                        return
            store.append(info)
    if not container:
        print("No such order ID found")
        return
    with open ("orders.txt", "w") as file:
        for line in store:
            file.write(f"{line[0]},{line[1]},{line[2].title()},{line[3].title()},{line[4]},{line[5]}\n")
    print("Order updated successfully!")

def delete_order(order_id, username):
    info = []
    store = []
    with open("orders.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if not (order_id == info[0] and username == info[1]):
                store.append(info)
    with open ("orders.txt", "w") as file:
        for line in store:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]}\n")
    print("Order deleted successfully!")

# Send Feedback Function
def send_feedback(name):
    cate = input("Enter the category: ")
    food_item = input("Enter the food item you want to provide feedback on: ")
    comment = input("Enter your feedback: ")
    rating = input("Enter your rating (1-5): ")
    with open("customer_feedback.txt", "a") as file:
        file.write(f"{name.strip()},{cate.strip()},{food_item.strip()},{comment.strip()},{rating.strip()}\n")
    print("Feedback submitted successfully!")

# Update Customer Profile Function
def update_customer_profile(name, username):
    data = []
    found = False
    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[1] == username:
                found = True
                print("\nWhat would you like to edit?")
                print("1. Name")
                print("2. Username")
                print("3. Email")
                print("4. Password")
                print("5. Back")

                selection = int(input("Choose the option you want to edit: "))

                match selection:
                    case 1:
                        info[0] = input("\nEnter the new name: ")
                    case 2:
                        info[1] = input("\nEnter the new username: ")
                    case 3:
                        info[2] = input("\nEnter the new email: ")
                    case 4:
                        info[3] = input("\nEnter the new password: ")
                    case 5:
                        print("Back to menu\n")
                        return
                    case _:
                        print("Invalid selection! Please choose a valid option.")

            data.append(info)

    if found:
        with open("user.txt", "w") as file:
            for line in data:
                file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")
        print("Profile updated successfully!")
    else:
        print("No matching user found.")


#---------------------------------------////////////////////////////////////////////////////////

main()
