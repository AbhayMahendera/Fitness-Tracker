import json
import os
import visualization
import recommendations


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

# ---------------------------- Log in Data ---------------------------- #

def log_data():
    return 0

# ---------------------------- Display Logs ---------------------------- #

def show_logs():
    return 0

# ---------------------------- More Options ---------------------------- #

def more_option():
    while True:
        a = input("Key in 1 to see more options.\nKey in 2 to exit: ")
        if a == '1':
            while True:
                b = input("Press 1 to log data.\n Press 2 to view your daily logs.\nPress 3 to see your health trends.\nPress 4 to see diet recommendations for you.\nPress 5 to exit: ")
                if b == '1':
                    log_data()
                    break
                elif b =='2':
                    show_logs()
                    break
                elif b == '3':
                    visualization.visualize()
                    break
                elif b == '4':
                    recommendations.show_recommendations()
                    break
                elif b == '5':
                    return
                else:
                    print("Wrong input received. Please try again.")
        elif a == '2':
            return
        else:
            print("Invalid choice. Please try again.")


    
