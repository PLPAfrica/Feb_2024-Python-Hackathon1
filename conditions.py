# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

# This requires use of conditional statemnt. 

# step 1 --> create a variable user input that prompts user for their age and convert user input into an int through typecasting.

user_age = int(input("Enter age (in numbers):"))

# step 2 --> introduce conditionals if else. 

if user_age >= 18:
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")

"""
    the above program will print a message to the screen depending on the user's age input. 
"""