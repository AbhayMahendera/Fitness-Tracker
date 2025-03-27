import json
import os
from auth import hash_password

# ---------------------------- Make New User Data ---------------------------- #

def make_new_user():
    username = input("Type in a username for your account: ")

    filename = os.path.join("data", "users", f"{username}.json")
    
    # Ensure the directory exists
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
        # Hashing and Storing the password
    password_hashed = hash_password(password)
    print(f"Hashed password: {password_hashed}")

    filename = os.path.join("data", "user_db.json")

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
    
    # Ensure the directory exists
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


make_new_user()


# ---------------------------- Fetch User Data ---------------------------- #

def get_user_data(username):
    filename = os.path.join("data", "users", f"{username}.json")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            user = json.load(file)
            
            details = user.get("details", {})
            logs = user.get("daily_logs", [])
            latest_log = logs[-1] if logs else None
            
            result = (f"====================================\n"
                      f"        Welcome, {details.get('full_name', 'User')}!\n"
                      f"====================================\n\n"
                      f"Current Info:\n"
                      f"   - Age: {details.get('age', 'N/A')} years\n"
                      f"   - Weight: {details.get('weight', 'N/A')} kg\n"
                      f"   - Height: {details.get('height', 'N/A')} m\n\n")
            
            if latest_log:
                result += (f"Latest Daily Log:\n"
                           f"   Date: {latest_log.get('date', 'N/A')}\n"
                           f"   Activity: {latest_log.get('activity', 'N/A')}\n"
                           f"   Slept for {latest_log.get('sleep_hours', 'N/A')} hours\n"
                           f"   Consumed {latest_log.get('estimated_calories_consumed', 'N/A')} calories\n")
            else:
                result += "No daily logs available.\n"
            
            return result
    except FileNotFoundError:
        return "Error: JSON file not found."
    except json.JSONDecodeError:
        return "Error: Invalid JSON format."


# ---------------------------- Update User Data ---------------------------- #

def update_user_data(username):
    filename = os.path.join("data", "users", f"{username}.json")

    try:
        with open(filename, "r+", encoding="utf-8") as file:
            user = json.load(file)

            while True:
                print("\n===============================")
                print("     Update User Info Menu     ")
                print("===============================")
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Weight")
                print("4. Update Height")
                print("5. Update Activity Level")
                print("6. Exit and return to main")
                choice = input("Enter the number of the information you want to update: ")

                if choice == '1':
                    new_name = input("Enter the new name: ")
                    user["details"]["full_name"] = new_name
                    print(f"Name updated to: {new_name}")

                elif choice == '2':
                    while True:
                        try:
                            new_age = int(input("Enter the new age: "))
                            if new_age <= 0:
                                raise ValueError("Age must be a positive integer.")
                            user["details"]["age"] = new_age
                            print(f"Age updated to: {new_age}")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}. Please enter a valid age.")

                elif choice == '3':
                    while True:
                        try:
                            new_weight = float(input("Enter the new weight (kg): "))
                            if new_weight <= 0:
                                raise ValueError("Weight must be a positive number.")
                            user["details"]["weight"] = new_weight
                            print(f"Weight updated to: {new_weight} kg")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}. Please enter a valid weight.")

                elif choice == '4':
                    while True:
                        try:
                            new_height = float(input("Enter the new height (m): "))
                            if new_height <= 0:
                                raise ValueError("Height must be a positive number.")
                            user["details"]["height"] = new_height
                            print(f"Height updated to: {new_height} m")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}. Please enter a valid height.")

                elif choice == '5':
                    
                    while True:
                        new_activity_level = input("Enter the new activity level (low, moderate, high): ").lower()
                        if new_activity_level in ['low', 'moderate', 'high']:
                            user["details"]["activity_level"] = new_activity_level
                            print(f"Activity level updated to: {new_activity_level}")
                            break
                        else:
                            print("Invalid input. Please enter one of the following options: low, moderate, high.")

                elif choice == '6':
                    file.seek(0)
                    json.dump(user, file, indent=4)
                    file.truncate()
                    print("\nChanges saved. Returning to the main function...")
                    break  

                else:
                    print("\nInvalid choice. Please try again.")
    except FileNotFoundError:
        print("Error: JSON file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
