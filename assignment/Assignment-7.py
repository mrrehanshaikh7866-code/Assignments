#A nutrition app needs to calculate daily caloric intake. Write a Python script that:
#Defines a function calculate_calories(carbs, fats, proteins) that calculates total calories based on grams of
#carbs, fats, and proteins (1 gram of carbs = 4 calories, 1 gram of fats = 9 calories, 1 gram of proteins = 4
#calories).
#Uses this function to input the grams of carbs, fats, and proteins consumed in a day and prints the total
#caloric intake.

def calculate_calories(carbs, fats, proteins):
    total_calories = (carbs * 4) + (fats * 9) + (proteins * 4)
    return total_calories


carbs = float(input("Enter grams of carbohydrates: "))
fats = float(input("Enter grams of fats: "))
proteins = float(input("Enter grams of proteins: "))

total = calculate_calories(carbs, fats, proteins)

print("Total daily caloric intake:", total, "calories")