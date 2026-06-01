# FitCalc Pro

A terminal-based personal fitness calculator built with Python. The user enters their personal stats and workout data, and the program calculates their BMI, recommended daily calorie intake, workout performance scores, and delivers a complete fitness report — all inside the terminal.

This project was built as a hands-on beginner Python project covering real-world programming concepts from the ground up.

---

## Features

- BMI calculation using two different methods and result verification
- BMI status classification — Underweight, Normal, Overweight, Obese
- Daily calorie target based on weight, height, age, and activity level
- Workout score analysis — best, worst, gap, average, and fitness index
- Even/odd workout day check
- Advanced math calculations using Python's math module
- Full personal fitness report printed at the end

---

## How to Run

Make sure Python is installed on your machine.

```bash
python fitcalc_pro.py
```

Follow the prompts in the terminal. Enter your name, age, gender, weight, height, activity level, workout days, and three exercise scores.

---

## Sample Output

```
Welcome to FitCalc Pro
----------------------
Enter your name: Alex
Enter your age: 24
Enter your gender (male/female): male
Enter your weight (kg): 78.5
Enter your height (m): 1.75
Are you physically active? (yes/no): yes
How many days did you work out this week? 4
Enter Exercise Score 1 (out of 100): 88
Enter Exercise Score 2 (out of 100): 76
Enter Exercise Score 3 (out of 100): 91

BMI Calculation
---------------
BMI (using **)  : 25.63
BMI (using pow) : 25.63
Result Match    : True

BMI Status
----------
BMI Score : 25.63
Status    : Overweight

Calorie Intake
--------------
Base Metabolic Rate  : 1994 kcal
Activity Adjustment  : +398.8 kcal
Workout Day Bonus    : +200 kcal
Final Calorie Target : 2592.8 kcal

Workout Score Analysis
----------------------
Score 1       : 88
Score 2       : 76
Score 3       : 91

Best Score    : 91
Worst Score   : 76
Score Gap     : 15
Average Score : 85.0
Fitness Index : 9.22

Workout Days This Week: 4
Result: Even number of workout days — good symmetry in your schedule.

Advanced Calculations
---------------------
Body Estimate (pi-based)   : 246.62
Metabolic Growth (e-based) : 2.72
Safe Minimum Weight Goal   : 70 kg

============================
     FitCalc Pro Report
============================
Name             : Alex
Age              : 24
Weight           : 78.5 kg
Height           : 1.75 m
Active           : True

BMI              : 25.63
BMI Status       : Overweight

Calorie Target   : 2592.8 kcal

Best Score       : 91
Worst Score      : 76
Fitness Index    : 9.22
Fitness Level    : Strong

Workout Days     : 4 (Even)
============================
     Keep pushing, Alex.
============================
```

---

## Concepts Learned & Applied

### print()
Used throughout the program to display section headers, labels, results, and the final fitness report in the terminal.

### Comments
Every section of the code is organized with inline comments to explain what each block does and why.

### Variables
All user data and calculated results are stored in clearly named variables. Each variable holds one specific piece of information — name, age, weight, BMI, score, and so on.

### Data Types

| Type | Example Used |
|------|-------------|
| String | User name, gender, active input |
| Integer | Age, workout days, exercise scores |
| Float | Weight, height, BMI, calorie values |
| Boolean | BMI match result, active status |

### F-Strings
Used to embed variable values directly into printed messages without string concatenation. Every output line in this project uses an f-string.

```python
print(f"BMI Score : {bmi}")
print(f"Status    : {status}")
```

### type()
Used in the Data Type Check section to verify that all input values were correctly converted to their expected types before any calculations begin.

### Explicit Type Conversion
All user input comes in as a string by default. Each value is explicitly converted to the correct type — `int()` for age and workout days, `float()` for weight and height, and a comparison check for the boolean active status.

### input()
Used to collect all user data from the terminal at the start of the program.

### Arithmetic Operators

| Operator | Used For |
|----------|---------|
| `+` | Adding calorie adjustments |
| `-` | Subtracting age factor in BMR |
| `*` | Multiplying weight and activity bonus |
| `/` | Dividing scores for average |
| `**` | Squaring height for BMI |
| `%` | Checking even or odd workout days |

### Augmented Assignment Operator
Used to add calorie adjustments on top of the base metabolic rate step by step rather than writing one long formula.

```python
final_calorie += activity_adjustment
final_calorie += workout_bonus
```

### round()
Used to clean up decimal results to a readable number of decimal places — BMI to 2 places, average score to 1 place, fitness index to 2 places.

### abs()
Used to ensure all user inputs are positive numbers, and to calculate the absolute gap between best and worst scores regardless of subtraction order.

### pow()
Used as an alternative to `**` for squaring height during BMI calculation. Both methods produce the same result, which is then verified using `==`.

### max() and min()
Used to find the highest and lowest exercise scores out of the three the user entered.

```python
best_score  = max(score_1, score_2, score_3)
worst_score = min(score_1, score_2, score_3)
```

### import math
The built-in Python math module is imported at the top of the file to access advanced mathematical functions and constants.

### math.pi
Used in the body estimate calculation — the value of π (approximately 3.14159) is multiplied by the user's weight.

### math.e
Used as a metabolic growth factor — Euler's number (approximately 2.71828) is rounded and displayed as a reference value.

### math.sqrt()
Used to calculate the fitness index by taking the square root of the average exercise score.

```python
fitness_index = round(math.sqrt(average_score), 2)
```

### math.ceil()
Used to round the Base Metabolic Rate up to the nearest whole number. Ceiling is used here because calorie recommendations should always round up — never under.

### math.floor()
Used to calculate the safe minimum weight goal by rounding the 90% weight value down to the nearest whole number.

### if / elif / else
Used in multiple places throughout the program:
- To classify BMI status into four categories
- To assign a fitness level based on the fitness index
- To determine whether workout days are even or odd
- To set the active status boolean from the user's yes/no input

### Comparison Operators

| Operator | Used For |
|----------|---------|
| `>=` | Checking BMI thresholds |
| `==` | Verifying BMI match, checking yes/no input |
| `>` | Comparing fitness index ranges |
| `<` | Underweight BMI check |

---

## Project Structure

```
fitcalc-pro/
│
├── fitcalc_pro.py   # Main program file
└── README.md        # Project documentation
```

---

## Built With

- Python 3
- math module (standard library)

---

## Author

Built as a beginner Python learning project — covering core programming fundamentals through a practical, real-world fitness application.
