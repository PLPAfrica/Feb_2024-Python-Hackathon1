# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

# Identify user by name and ID_Number
name = str(input("What is your name? "))
id_number = input("What is your ID number? ")  # Corrected variable name

# Ask the user's age to determine voting eligibility
age = int(input("What is your age? "))

if age >= 18:
    # Welcome the user by name and inform about eligibility
    print(f"Welcome, {name}. You are eligible to vote.")
else:
    # Inform the user about ineligibility if age requirement is not met
    print(f"Sorry, {name}. You are not eligible to vote yet.")

    