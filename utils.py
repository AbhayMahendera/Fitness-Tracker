import json
import os
import visualization
import recommendations
from datetime import datetime
from calculations import calculate_bmi, calculate_bmr, calculate_tdee



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

def log_data(username):
    filename = os.path.join("data", "users", f"{username}.json")
    try:
    
        with open(filename, "r+", encoding="utf-8") as file:
          
            user = json.load(file)

        
            current_weight = user["details"]["weight"]
            current_height = user["details"]["height"]
            current_age = user["details"]["age"]
            gender = user["details"]["gender"]
            
            activity_level = input("Enter today's activity level (low, moderate, high): ").lower()
            estimated_calories = int(input("Enter estimated calories consumed: "))
            sleep_hours = float(input("Enter hours slept: "))
            stress = input("Were you stressed today? (yes/no): ").strip().lower() == "yes"
            
            log_entry = {
                "date": datetime.today().strftime('%Y-%m-%d'),
                "activity": activity_level,
                "estimated_calories_consumed": estimated_calories,
                "sleep_hours": sleep_hours,
                "stress": stress
            }
            
            user["daily_logs"].append(log_entry)

            bmi = calculate_bmi(current_weight, current_height)
            bmr = calculate_bmr(current_weight, current_height, current_age, gender)
            tdee = calculate_tdee(bmr, activity_level)

            user["details"]["metrics"] = {
                "bmi": bmi,
                "bmr": bmr,
                "tdee": tdee
            }

            file.seek(0)
            json.dump(user, file, indent=4)
            file.truncate() 

            print(f"\nMetrics for {username}:")
            print(f"BMI: {bmi:.2f}")
            print(f"BMR: {bmr:.2f} kcal/day")
            print(f"TDEE: {tdee:.2f} kcal/day")
            print("✅ Daily log recorded successfully!")

    except FileNotFoundError:
        print(f"Error: {username}.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
# ---------------------------- Display Logs ---------------------------- #

def show_logs(username):
    filename = os.path.join("data", "users", f"{username}.json")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            user = json.load(file)
            logs = user.get("daily_logs", [])[-5:]
            print("\n------------------------------------------")
            print("        Recent Logs (Last 5 Entries)       ")
            print("------------------------------------------")
            if not logs:
                print("No logs available.")
                print("------------------------------------------")
                return
            for log in logs:
                print(f"Date           : {log.get('date', 'N/A')}")
                print(f"Activity       : {log.get('activity', 'N/A').capitalize()}")
                print(f"Calories       : {log.get('estimated_calories_consumed', 'N/A')} kcal")
                print(f"Sleep         : {log.get('sleep_hours', 'N/A')} hours")
                print(f"Stress Level   : {'Yes' if log.get('stress', False) else 'No'}")
                print("------------------------------------------")
    except FileNotFoundError:
        print("Error: User file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")



# ---------------------------- Update Height and Weight ---------------------------- #


def update_height_weight(username):
    filename = os.path.join("data", "users", f"{username}.json")
    try:
        with open(filename, "r+", encoding="utf-8") as file:
            user = json.load(file)

            new_weight = float(input("Enter your new weight (kg): "))
            new_height = float(input("Enter your new height (m): "))

            user["details"]["weight"] = new_weight
            user["details"]["height"] = new_height

            bmi = calculate_bmi(new_weight, new_height)
            bmr = calculate_bmr(new_weight, new_height, user["details"]["age"], user["details"]["gender"])
            tdee = calculate_tdee(bmr, user["details"]["activity_level"])

            user["details"]["metrics"] = {
                "bmi": bmi,
                "bmr": bmr,
                "tdee": tdee
            }

            file.seek(0)
            json.dump(user, file, indent=4)
            file.truncate()  

            print("✅ Height and weight updated successfully!")
            print(f"New BMI: {bmi:.2f}")
            print(f"New BMR: {bmr:.2f} kcal/day")
            print(f"New TDEE: {tdee:.2f} kcal/day")
    except FileNotFoundError:
        print(f"Error: {username}.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")


# ---------------------------- More Options ---------------------------- #


def more_option(username):
    def print_menu():
        print("\n=========================")
        print("        Options        ")
        print("=========================")
        print("1. Log data")
        print("2. Show logs")
        print("3. Show trends")
        print("4. Show recommendations")
        print("5. Update height and weight")
        print("6. Exit")

    print_menu() 

    while True:
        choice = input("Enter your choice (1-6), or press Enter to show options again: ").strip()

        if choice == '':
            print_menu()

        elif choice == '1':
            log_data(username)

        elif choice == '2':
            show_logs(username)

        elif choice == '3':
            visualization.visualize(username)

        elif choice == '4':
            recommendations.show_recommendations(username)

        elif choice == '5':
            update_height_weight(username)

        elif choice == '6':
            print("👋 Exiting the options menu. See you soon!")
            break

        else:
            print("❌ Invalid choice. Press Enter to see the menu again.")

