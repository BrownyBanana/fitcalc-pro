import math

# ─── Welcome ───────────────────────────────────────────────
print("Welcome to FitCalc Pro")
print("----------------------")

# ─── User Input ────────────────────────────────────────────
name   = input("Enter your name: ")
age    = abs(int(input("Enter your age: ")))
gender = input("Enter your gender (male/female): ")
weight = abs(float(input("Enter your weight (kg): ")))
height = abs(float(input("Enter your height (m): ")))
active = input("Are you physically active? (yes/no): ")
workout = abs(int(input("How many days did you work out this week? ")))
score_1 = abs(int(input("Enter Exercise Score 1 (out of 100): ")))
score_2 = abs(int(input("Enter Exercise Score 2 (out of 100): ")))
score_3 = abs(int(input("Enter Exercise Score 3 (out of 100): ")))

# ─── Data Type Check ───────────────────────────────────────
print("\nData Type Check")
print("---------------")
is_active = bool(active)
print(f"Name type   : {type(name)}")
print(f"Age type    : {type(age)}")
print(f"Weight type : {type(weight)}")
print(f"Height type : {type(height)}")
print(f"Active type : {type(is_active)}")

# ─── BMI Calculation ───────────────────────────────────────
bmi_1 = round(weight / height ** 2, 2)
bmi_2 = round(weight / math.pow(height, 2), 2)
bmi   = bmi_2
bmi_match = bmi_1 == bmi_2

print("\nBMI Calculation")
print("---------------")
print(f"BMI (using **)  : {bmi_1}")
print(f"BMI (using pow) : {bmi_2}")
print(f"Result Match    : {bmi_match}")

# ─── BMI Status ────────────────────────────────────────────
print("\nBMI Status")
print("----------")
print(f"BMI Score : {bmi}")

if bmi >= 30.0:
    status = "Obese"
elif bmi >= 25.0:
    status = "Overweight"
elif bmi >= 18.5:
    status = "Normal"
else:
    status = "Underweight"

print(f"Status    : {status}")

# ─── Calorie Intake ────────────────────────────────────────
bmr = math.ceil((10 * weight) + (6.25 * height * 100) - (5 * age) + 5)
activity_adjustment = round(bmr * 0.20, 2)
workout_bonus       = round(workout * 50, 2)
final_calorie       = round(bmr + activity_adjustment + workout_bonus, 2)

print("\nCalorie Intake")
print("--------------")
print(f"Base Metabolic Rate  : {bmr} kcal")
print(f"Activity Adjustment  : +{activity_adjustment} kcal")
print(f"Workout Day Bonus    : +{workout_bonus} kcal")
print(f"Final Calorie Target : {final_calorie} kcal")

# ─── Workout Score Analysis ────────────────────────────────
best_score    = max(score_1, score_2, score_3)
worst_score   = min(score_1, score_2, score_3)
score_gap     = abs(best_score - worst_score)
average_score = round((score_1 + score_2 + score_3) / 3, 1)
fitness_index = round(math.sqrt(average_score), 2)

print("\nWorkout Score Analysis")
print("----------------------")
print(f"Score 1       : {score_1}")
print(f"Score 2       : {score_2}")
print(f"Score 3       : {score_3}")
print()
print(f"Best Score    : {best_score}")
print(f"Worst Score   : {worst_score}")
print(f"Score Gap     : {score_gap}")
print(f"Average Score : {average_score}")
print(f"Fitness Index : {fitness_index}")

# ─── Workout Day Check ─────────────────────────────────────
even = workout % 2 == 0
day_label = "Even" if even else "Odd"

print(f"\nWorkout Days This Week: {workout}")
if even:
    print("Result: Even number of workout days — good symmetry in your schedule.")
else:
    print("Result: Odd number of workout days — consider adding one more day for balance.")

# ─── Advanced Calculations ─────────────────────────────────
body_estimate     = round(math.pi * weight, 2)
metabolic_growth  = round(math.e, 2)
weight_goal       = math.floor(weight * 0.90)

print("\nAdvanced Calculations")
print("---------------------")
print(f"Body Estimate (pi-based)   : {body_estimate}")
print(f"Metabolic Growth (e-based) : {metabolic_growth}")
print(f"Safe Minimum Weight Goal   : {weight_goal} kg")

# ─── Fitness Level ─────────────────────────────────────────
if fitness_index >= 9.5:
    level = "Elite"
elif fitness_index >= 8.0:
    level = "Strong"
elif fitness_index >= 6.5:
    level = "Average"
else:
    level = "Needs Improvement"

# ─── Active Status ─────────────────────────────────────────
is_active_status = active.strip().lower() == "yes"

# ─── Final Report ──────────────────────────────────────────
print("\n============================")
print("     FitCalc Pro Report")
print("============================")
print(f"Name             : {name}")
print(f"Age              : {age}")
print(f"Weight           : {weight} kg")
print(f"Height           : {height} m")
print(f"Active           : {is_active_status}")
print(f"\nBMI              : {bmi}")
print(f"BMI Status       : {status}")
print(f"\nCalorie Target   : {final_calorie} kcal")
print(f"\nBest Score       : {best_score}")
print(f"Worst Score      : {worst_score}")
print(f"Fitness Index    : {fitness_index}")
print(f"Fitness Level    : {level}")
print(f"\nWorkout Days     : {workout} ({day_label})")
print("============================")
print(f"     Keep pushing, {name}.")
print("============================")