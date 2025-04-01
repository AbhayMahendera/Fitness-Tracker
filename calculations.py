# calculations.py

def calculate_bmi(current_weight, current_height):
    bmi = current_weight / (current_height ** 2)
    return bmi

def calculate_bmr(current_weight, current_height, current_age, gender):
    height_cms = current_height * 100
    if gender == 'male':
        bmr = (10 * current_weight) + (6.25 * height_cms) - (5 * current_age) + 5
    else:
        bmr = (10 * current_weight) + (6.25 * height_cms) - (5 * current_age) - 161
    return bmr

def calculate_tdee(bmr, activity):
    if activity == 'sedentary':
        tdee = bmr * 1.2
    elif activity == 'moderate':
        tdee = bmr * 1.55
    else:
        tdee = bmr * 1.9
    return tdee
