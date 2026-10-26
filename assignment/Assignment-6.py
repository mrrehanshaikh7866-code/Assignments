#Build a program that prompts the user to enter passwords until they enter "stop". For
#each password entered, check if it meets the following criteria:
#● At least 8 characters long
#● Contains both uppercase and lowercase letters
#● Contains at least one digit. Print a message indicating whether each password is strong or
#weak based on these criteria.
while True:
    password = input("Enter a password (or 'stop' to exit): ")

    if password.lower() == "stop":
        print("Program ended.")
        break

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if len(password) >= 8 and has_upper and has_lower and has_digit:
        print("Strong password")
    else:
        print("Weak password")