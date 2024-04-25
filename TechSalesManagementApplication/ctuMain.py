from ctuClass import ctuStock

# Shop objects
shop1 = ctuStock("Default", "Default", 0, 0, 0)
shop2 = ctuStock("Default", "Default", 0, 0, 0)
shop3 = ctuStock("Default", "Default", 0, 0, 0)
shop4 = ctuStock("Default", "Default", 0, 0, 0)

# Shop names
shop1.set_shop_name("Default")
shop2.set_shop_name("Default")
shop3.set_shop_name("Default")
shop4.set_shop_name("Default")


# Displaying the shop menu
def display_shop_menu():
    print("Welcome to CTU Technologies")
    print("1. Shop Management")
    print("2. Sales")
    print("3. Returns")
    print("4. Stock")
    print("99. Exit")


# Function for main menu
def main():
    display_shop_menu()

    while True:
        choice = input("Select an option or 99 to exit: ")

        if choice == "1":
            shop_management()
        elif choice == "2":
            sales()
        elif choice == "3":
            returns()
        elif choice == "4":
            stock()
        elif choice == "99":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Function to display sales menu
def display_sales_menu():
    print("Sales Menu:")


# Function to display shop management menu
def display_shop_management_menu():
    print("Shop Management Menu:")
    print("1. Change shop Name")
    print("2. Change shop Location")
    print("3. Display current shops")
    print("4. Display all shops information")
    print("0. Back")


# Function to display stock menu
def display_stock_menu():
    print("Stock Menu:")
    print("1. Display stock")
    print("2. Add stock")
    print("0. Back")


# Function to change shop name
def change_shop_name(selected_shop):
    new_name = input("Type the new Shop name: ")
    success = selected_shop.set_shop_name(new_name)

    if success:
        print("Shop name was successfully changed to " + new_name)
    else:
        print("Invalid shop selected.")


# Function to change sop location
def change_shop_location(selected_shop):
    new_location = input("Enter a location Free State, Gauteng, KZN, Limpopo: ")
    success = selected_shop.set_shop_location(new_location)

    if success:
        print("Shop location was successfully changed to ", new_location)
    else:
        print("Invalid shop selected.")


# Function to display all shops
def display_all_shops():
    print("-----------------")
    print("Shop information:")

    print("Shop Name:", shop1.get_shop_name())
    print("Shop Location:", shop1.get_shop_location())
    print("Number of Customers:", shop1.get_number_of_customers())
    print("Current Sales:", shop1.get_current_sales())
    print("Returns:", shop1.get_returns())

    print("----------------- \n-----------------")

    print("Shop Name:", shop2.get_shop_name())
    print("Shop Location:", shop2.get_shop_location())
    print("Number of Customers:", shop2.get_number_of_customers())
    print("Current Sales:", shop2.get_current_sales())
    print("Returns:", shop2.get_returns())

    print("----------------- \n-----------------")

    print("Shop Name:", shop3.get_shop_name())
    print("Shop Location:", shop3.get_shop_location())
    print("Number of Customers:", shop3.get_number_of_customers())
    print("Current Sales:", shop3.get_current_sales())
    print("Returns:", shop3.get_returns())

    print("----------------- \n-----------------")

    print("Shop Name:", shop4.get_shop_name())
    print("Shop Location:", shop4.get_shop_location())
    print("Number of Customers:", shop4.get_number_of_customers())
    print("Current Sales:", shop4.get_current_sales())
    print("Returns:", shop4.get_returns())

    print("-----------------")


# Function to display current shops
def display_current_shops():
    print("Current Shops:")
    if shop1.get_shop_name() != "":
        print(shop1.get_shop_name(), ",", shop1.get_shop_location())
    if shop2.get_shop_name() != "":
        print(shop2.get_shop_name(), ",", shop2.get_shop_location())
    if shop3.get_shop_name() != "":
        print(shop3.get_shop_name(), ",", shop3.get_shop_location())
    if shop4.get_shop_name() != "":
        print(shop4.get_shop_name(), ",", shop4.get_shop_location())


# Function to select shop
def select_shop():
    while True:
        print("Change Shop name: ")
        print("1.", shop1.get_shop_name())
        print("2.", shop2.get_shop_name())
        print("3.", shop3.get_shop_name())
        print("4.", shop4.get_shop_name())
        choice = input("Select an option: ")

        if choice == "1":
            return shop1
        elif choice == "2":
            return shop2
        elif choice == "3":
            return shop3
        elif choice == "4":
            return shop4
        else:
            print("Invalid shop number entered. Please try again.\n")


# Function to select shop location
def select_location():
    while True:
        print("Change Shop location: ")
        print("Select Shop")
        print("1.", shop1.get_shop_name(), ",", shop1.get_shop_location())
        print("2.", shop2.get_shop_name(), ",", shop2.get_shop_location())
        print("3.", shop3.get_shop_name(), ",", shop3.get_shop_location())
        print("4.", shop4.get_shop_name(), ",", shop4.get_shop_location())
        choice = input("Select an option: ")

        if choice == "1":
            return shop1
        elif choice == "2":
            return shop2
        elif choice == "3":
            return shop3
        elif choice == "4":
            return shop4
        else:
            print("Invalid shop number entered. Please try again.\n")


# Function for Shop management
def shop_management():
    while True:
        display_shop_management_menu()
        choice = input("Select an option: ")

        if choice == "1":
            selected_shop = select_shop()
            if selected_shop:
                change_shop_name(selected_shop)
        elif choice == "2":
            selected_shop = select_location()
            if selected_shop:
                change_shop_location(selected_shop)
        elif choice == "3":
            display_current_shops()
        elif choice == "4":
            display_all_shops()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.\n")


# Function for Sales
def sales():
    current_sales = 0

    while True:
        display_sales_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Sales:", current_sales)
        elif choice == "2":
            pass
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.\n")


# Function for Returns
def returns():
    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.\n")


# Function for Stock
def stock():
    while True:
        display_stock_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.\n")


main()
