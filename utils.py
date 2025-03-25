import json
import os


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





