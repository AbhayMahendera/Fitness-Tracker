import bcrypt
import os
import json
import utils

def hash_password(password):
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def verify_password(entered_password, stored_hash):
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hash.encode('utf-8'))


                            # ---------------------------- Sign Up ---------------------------- #

def signup():
    username = input("Type in a username for your account: ")

    filename = os.path.join("data", "users", f"{username}.json")

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    password = None
    confirm_password = "Undefined"

    while password != confirm_password:
        password = input("Enter a password for your account: ")
        confirm_password = input("Please enter your password again: ")
    
        if password != confirm_password:
            print("\nPasswords do not match. Please try again.\n")

    print("\nPassword set successfully!\n")

                                 #---------------------------Hashing and Storing the password---------------------------
 
    password_hashed = hash_password(password)
    print(f"Hashed password: {password_hashed}")

    filename = os.path.join("data", "user_db.json")

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {} 
    else:
        data = {}

    data[username] = password_hashed

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

                                         # -------------------------------------- #
    filename = os.path.join("data", "users", f"{username}.json")
    

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    full_name = input("Enter your full name: ")
    gender = input("Enter your gender: ")

    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                raise ValueError("Age must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid age.")

    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid weight.")

    while True:
        try:
            height = float(input("Enter your height (m): "))
            if height <= 0:
                raise ValueError("Height must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid height.")

    while True:
        activity_level = input("Enter your activity level (low, moderate, high): ").lower()
        if activity_level in ['low', 'moderate', 'high']:
            break
        else:
            print("Invalid input. Please enter one of the following options: low, moderate, high.")

    
    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email format. Please enter a valid email.")

    user_data = {
        "username": username,
        "details": {
            "full_name": full_name,
            "gender": gender,
            "age": age,
            "weight": weight,
            "height": height,
            "activity_level": activity_level,
            "email": email
        },
        "daily_logs": [] 
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(user_data, file, indent=4)

    print(f"\nUser '{username}' has been created successfully!\n")


# ----------------------------  Log in ---------------------------- #

def login():
    filename = os.path.join("data", "user_db.json")

    if not os.path.exists(filename):
        print("User database not found!")
        return

    try:
        with open(filename, "r") as file:
            users = json.load(file)
    except json.JSONDecodeError:
        print("Error reading user database!")
        return

    while True: 
        username = input("\nPlease key in your username: ")
        if username not in users:
            print("Invalid username! Try again.")
            continue 

        password = input("\nPlease key in your password: ")
        stored_hash = users[username]

        if verify_password(password, stored_hash):
            print("Login successful!")
            print(utils.get_user_data(username))
            
            utils.more_option(username)


        else:
            print("Incorrect password! Try again.")




