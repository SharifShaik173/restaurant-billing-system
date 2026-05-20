# ---------- Bill Splitting & Payment System for Restaurants ----------

# ---------------- USER DATA ----------------
users_info = {
    1: {"name": "sam", "password": 1234, "email": "sam@gmail.com"},
    2: {"name": "ram", "password": 4567, "email": "ram@gmail.com"}
}

# ---------------- MENU DATA ----------------
menu = {
    1: {"name": "Pizza", "price": 199, "stock": 100},
    2: {"name": "Cheese Sweet Corn", "price": 379, "stock": 100},
    3: {"name": "Double Cheese Pizza", "price": 399, "stock": 100},
    4: {"name": "Fresh Veggie", "price": 339, "stock": 100},
    5: {"name": "Peppy Paneer", "price": 459, "stock": 100}
}

# ---------------- SHOW MENU ----------------
def show_menu():
    print("\n-------- Available Items --------")
    for key, item in menu.items():
        print(f"{key}. {item['name']} | Price: ₹{item['price']} | Stock: {item['stock']}")

# ---------------- ORDER FUNCTION ----------------
def order_items():
    cart = []

    while True:
        show_menu()

        try:
            choice = int(input("\nEnter item number: "))

            if choice not in menu:
                print("Invalid choice")
                continue

            item = menu[choice]

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print(" Quantity must be greater than 0")
                continue

            if quantity > item["stock"]:
                print(" Not enough stock")
                continue

            total_price = item["price"] * quantity

            cart.append({
                "name": item["name"],
                "quantity": quantity,
                "total": total_price
            })

            item["stock"] -= quantity

            print(f" {item['name']} added")

        except ValueError:
            print(" Enter valid numbers")
            continue

        cont = input("Add more items? (yes/no): ").lower()
        if cont != "yes":
            break

    # -------- BILL --------
    print("\n-------- BILL --------")
    grand_total = 0

    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['name']} | Qty: {item['quantity']} | ₹{item['total']}")
        grand_total += item["total"]

    print(f"\nTotal Bill: ₹{grand_total}")


# ---------------- LOGIN ----------------
def user_login():
    username = input("Username: ")
    password = int(input("Password: "))

    for user in users_info.values():
        if user["name"] == username and user["password"] == password:
            print("Login Successful")
            order_items()
            return

    print("Invalid Username or Password")


# ---------------- REGISTER ----------------
def user_register():
    username = input("Enter username: ")

    # check username exists
    for user in users_info.values():
        if user["name"] == username:
            print(" Username already exists")
            return

    password_1 = int(input("Enter password: "))
    password_2 = int(input("Confirm password: "))

    if password_1 != password_2:
        print("Passwords do not match")
        return

    email = input("Enter email: ")

    # check email exists
    for user in users_info.values():
        if user["email"] == email:
            print(" Email already exists")
            return

    new_id = len(users_info) + 1
    users_info[new_id] = {
        "name": username,
        "password": password_1,
        "email": email
    }

    print("Registration Successful")


# ---------------- MAIN MENU ----------------
while True:
    print("\n1. Login\n2. Register\n3. Exit")

    try:
        choice = int(input("Enter option: "))

        if choice == 1:
            user_login()
        elif choice == 2:
            user_register()
        elif choice == 3:
            print("Thank you!")
            break
        else:
            print(" Invalid option")

    except ValueError:
        print("Enter valid number")
