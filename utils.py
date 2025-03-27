import json
import os

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


    full_name = input("Enter your full name: ")
    gender = input("Enter your gender: ")

    
    while True:
        try:
            age = int(input("Enter your age: "))
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (m): "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers for age, weight, and height.")

    activity_level = input("Enter your activity level (low, moderate, high): ")
    email = input("Enter your email: ")

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
                    try:
                        new_age = int(input("Enter the new age: "))
                        user["details"]["age"] = new_age
                        print(f"Age updated to: {new_age}")
                    except ValueError:
                        print("Invalid input. Age must be a number.")

                elif choice == '3':
                    try:
                        new_weight = float(input("Enter the new weight (kg): "))
                        user["details"]["weight"] = new_weight
                        print(f"Weight updated to: {new_weight} kg")
                    except ValueError:
                        print("Invalid input. Weight must be a number.")

                elif choice == '4':
                    try:
                        new_height = float(input("Enter the new height (m): "))
                        user["details"]["height"] = new_height
                        print(f"Height updated to: {new_height} m")
                    except ValueError:
                        print("Invalid input. Height must be a number.")

                elif choice == '5':
                    new_activity_level = input("Enter the new activity level (e.g., low, moderate, high): ")
                    user["details"]["activity_level"] = new_activity_level
                    print(f"Activity level updated to: {new_activity_level}")

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
