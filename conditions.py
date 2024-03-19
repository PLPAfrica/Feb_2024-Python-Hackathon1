# Prompt the user to enter their age
while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid age.")

# Check if the age is greater than or equal to 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
-2