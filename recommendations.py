import json
import os


import sys
sys.stdout.reconfigure(encoding='utf-8')

def show_recommendations(username):
    user_file = os.path.join("data", "users", f"{username}.json")
    food_file = os.path.join("data", "food_db.json")

    try:
        with open(user_file, "r", encoding="utf-8") as f:
            user_data = json.load(f)

        with open(food_file, "r", encoding="utf-8") as f:
            food_data = json.load(f)

        metrics = user_data["details"]["metrics"]
        bmi = metrics.get("bmi", 0)
        bmr = metrics.get("bmr", 0)
        tdee = metrics.get("tdee", 0)

        foods = food_data.get("foods", [])
        recommended = []

        print("\n======= Personalized Food Recommendations =======")
        print(f"BMI: {bmi:.2f} | BMR: {bmr:.2f} | TDEE: {tdee:.2f}\n")

        if bmi >= 25:
            print("⚠️ You may be overweight. Here are some lean, high-protein, low-calorie foods:")
            recommended = [f for f in foods if f["protein_g"] >= 20 and f["fat_g"] <= 10 and f["calories"] <= 250]

        elif bmi < 18.5:
            print("⚠️ You may be underweight. Here are high-calorie, protein-rich foods to help you gain weight:")
            recommended = [f for f in foods if f["calories"] >= 300 and f["protein_g"] >= 15]

        else:
            print("✅ Your BMI is in the healthy range. Here's a balanced list of nutritious foods:")
            recommended = [f for f in foods if 200 <= f["calories"] <= 400 and f["protein_g"] >= 15]

        if not recommended:
            print("No suitable food found in the database.")
            return

        for food in recommended:
            print(f"- {food['name']}: {food['calories']} kcal | Protein: {food['protein_g']}g | Fat: {food['fat_g']}g | Carbs: {food['carbs_g']}g")

    except FileNotFoundError:
        print("Error: User or food database file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in one of the files.")


