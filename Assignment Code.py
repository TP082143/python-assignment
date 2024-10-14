#main function of the program
from select import select


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

#edit staff details function
def edit_staff():
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
                username = input("\nEnter username of the manager: ")
                email = input("Enter email of the manager: ")
                delete_staff_role(username, email, role)
                if delete_staff_role(username, email, role) == 1:
                    print("Successfully Deleted")
            elif selection == 3:
                break
            else:
                print("Wrong input! Please try again")
        except ValueError:
            print("Wrong input! Please try again")

def delete_staff_role(username, email, role):
    value = 0
    data = []
    info = []
    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if username != info[1] and email != info[2] and role != info[4]:
                value = 1
                data.append(info)
            else:
                value = 0
    with open("user.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")
    if value == 1:
        return 1
    else:
        print("No such data found!")

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
    report = []
    total = 0
    print("______________________________________________________________________________________________________________________")
    print(f"{month.title()} Sales Report:")
    with open("sales_report.txt", "r") as file:
        for line in file:
            report = line.strip().split(",")
            if report[0] == month.title():
                print(f"Customer ID - {report[1]} || Customer name - {report[2]} || Cuisine Type - {report[3]} || Dish - {report[4]} || Price - RM{report[5]}")
                total = total + float(report[5])
    print("______________________________________________________________________________________________________________________")
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
    month = ['','January','February','March','April','May','June','July','August','September','October','November','December']
    for i in range(1, 13):
        file = open("sales_report.txt", "r")
        file.seek(0)
        month_show = 0
        num = 1
        for line in file:
            lst = line.strip().split(",")
            if int(lst[6]) == i:
                if month_show == 0:
                    print("------------------------------------------------------------------------------------------------------------------------")
                    print(f"                                         ~~~~ {lst[0].upper()} Sales ~~~~                                          ")
                    month_show += 1
                print(f"{num}. Customer ID - {lst[1]} || Customer name - {lst[2]} || Cuisine Type - {lst[3]} || Dish - {lst[4]} || Price - RM{lst[5]}")
                num += 1
        file.close()
        if i == 12:
            print("------------------------------------------------------------------------------------------------------------------------")
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
            print(f"{i}. CUSTOMER_ID - {customer_feedback[0]} | CUSTOMER_NAME - {customer_feedback[1]} | FOOD - {customer_feedback[2]} | COMMENT - {customer_feedback[3]} | RATING - {customer_feedback[4]}")
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





#///////////////////-------------------------------- OMAR --------------------------------//////////////////////
# Functions for handling orders
def create_order(order_id, customer_name, dish):
    return {
        'order_id': order_id,
        'customer_name': customer_name,
        'dish': dish,
        'status': 'Pending'
    }


def update_order_status(orders, order_id, new_status):
    for order in orders:
        if order['order_id'] == order_id:
            if new_status.lower() in ["in progress", "completed"]:
                order['status'] = new_status
                print(f"Order {order_id} status updated to: {order['status']}")
            else:
                print("Invalid status. Please use 'In Progress' or 'Completed'.")
            break
    else:
        print(f"Order {order_id} not found.")


def view_orders(orders):
    if not orders:
        print("No orders placed yet.")
    else:
        print("Customer Orders:")
        for order in orders:
            print(
                f"- Order ID: {order['order_id']}, Customer: {order['customer_name']}, Dish: {order['dish']}, Status: {order['status']}")


# Functions for handling ingredients
def load_ingredients(filename):
    ingredients = []
    try:
        with open(filename, "r") as file:
            for line in file:
                ingredient_id, name, quantity = line.strip().split(",")
                ingredients.append({
                    'ingredient_id': int(ingredient_id),
                    'name': name,
                    'quantity': quantity  # Store as string
                })
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty inventory.")
    return ingredients


def save_ingredients(filename, ingredients):
    with open(filename, "w") as file:
        for ingredient in ingredients:
            file.write(f"{ingredient['ingredient_id']},{ingredient['name']},{ingredient['quantity']}\n")


def add_ingredient(ingredients):
    ingredient_id = int(input("Enter ingredient ID: "))

    # Check for duplicate ingredient ID
    for ingredient in ingredients:
        if ingredient['ingredient_id'] == ingredient_id:
            print("Ingredient ID already exists. Please choose a different ID.")
            return  # Exit the function if ID is duplicate

    name = input("Enter ingredient name: ")
    quantity = input("Enter ingredient quantity (can be string or int): ")  # Accept both types
    ingredients.append({
        'ingredient_id': ingredient_id,
        'name': name,
        'quantity': quantity  # Store quantity as string
    })
    save_ingredients("ingredients.txt", ingredients)
    print("Ingredient added successfully!")


def edit_ingredient(ingredients):
    ingredient_id = int(input("Enter ingredient ID to edit: "))
    for ingredient in ingredients:
        if ingredient['ingredient_id'] == ingredient_id:
            ingredient['name'] = input("Enter new ingredient name: ")
            quantity = input("Enter new ingredient quantity: ")
            ingredient['quantity'] = quantity  # Store quantity as string
            save_ingredients("ingredients.txt", ingredients)
            print("Ingredient updated successfully!")
            break
    else:
        print("Ingredient not found!")


def delete_ingredient(ingredients):
    ingredient_id = int(input("Enter ingredient ID to delete: "))
    for ingredient in ingredients:
        if ingredient['ingredient_id'] == ingredient_id:
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
            print(
                f"- ID: {ingredient['ingredient_id']}, Name: {ingredient['name']}, Quantity: {ingredient['quantity']}")


# User registration
def registration():
    chef_name = input("Enter your name: ")
    chef_username = input("Enter username: ")
    chef_password = input("Enter password: ")
    chef_email = input("Enter your Email: ")

    # Check for duplicate user ID
    with open("user.txt", "r") as file:
        for line in file:
            lst = line.strip().split(",")
            if lst[1] == chef_username:
                print("Username already exists. Please choose a different username.")
                return  # Exit the function if ID is duplicate

    with open("user.txt", "a") as file:
        file.write(f"{chef_name},{chef_username},{chef_email},{chef_password},chef\n")
    print("User registered successfully!\n")


# Function to update user profile
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

                # Update fields if new input is provided
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


# Main management system for logged-in users
def chef_management_menu(name, username):
    ingredients = load_ingredients("ingredients.txt")
    orders = []

    while True:
        print("\nManagement Menu:")
        print("1. Add Ingredient")
        print("2. Edit Ingredient")
        print("3. Delete Ingredient")
        print("4. View Ingredients")
        print("5. Add Order")
        print("6. Update Order Status")
        print("7. View Orders")
        print("8. Update Profile")  # Add option to update profile
        print("9. Logout")
        print("10. Exit")

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
            customer_name = input("Enter customer name: ")
            dish = input("Enter dish: ")
            orders.append(create_order(order_id, customer_name, dish))
        elif choice == "6":
            order_id = int(input("Enter order ID: "))
            new_status = input("Enter new status (In Progress/Completed): ")
            update_order_status(orders, order_id, new_status)
        elif choice == "7":
            view_orders(orders)
        elif choice == "8":
            update_profile_chef(username)  # Pass user ID for profile update
        elif choice == "9":
            print(f"Goodbye, {name}!")
            return  # Logs out the user and returns to the login screen
        elif choice == "10":
            print("Exiting program...")
            exit()
        else:
            print("Invalid choice. Please try again.")

#--------------------------------------------------------------------------------------------////////


main()
