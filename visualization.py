import json
import os
from tabulate import tabulate

import sys
sys.stdout.reconfigure(encoding='utf-8')

def visualize(username):
    filename = os.path.join("data", "users", f"{username}.json")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            user = json.load(file)

        logs = user.get("daily_logs", [])
        if not logs:
            print("No logs to visualize.")
            return

        logs = logs[-7:]  

        table = []
        for log in logs:
            date = log.get("date", "N/A")
            cal = log.get("estimated_calories_consumed", 0)
            sleep = log.get("sleep_hours", 0)
            stress = "💢 Yes" if log.get("stress") else "✅ No"
            activity = log.get("activity", "N/A").capitalize()

            cal_display = f"🔥 {cal:,} kcal"
            sleep_display = f"💤 {sleep:.1f} hrs"
            table.append([f"📅 {date}", cal_display, sleep_display, stress, activity])

        headers = ["📆 Date", "🔥 Calories", "😴 Sleep", "😬 Stress", "🏃‍♂️ Activity Level"]

        print("\n✨ 𝗬𝗼𝘂𝗿 𝗛𝗲𝗮𝗹𝘁𝗵 𝗟𝗼𝗴 (𝗣𝗮𝘀𝘁 7 𝗗𝗮𝘆𝘀) ✨\n")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid", stralign="center"))

        tdee = user["details"]["metrics"].get("tdee")
        if tdee:
            print(f"\n🔧 Your Target Daily Energy Expenditure (TDEE): **{tdee:.2f} kcal/day**")

        print("\n✅ Tip: Aim to keep stress low, sleep at least 6-7 hours, and balance your calories!\n")

    except FileNotFoundError:
        print("❌ User file not found.")
    except json.JSONDecodeError:
        print("❌ Invalid JSON format.")

