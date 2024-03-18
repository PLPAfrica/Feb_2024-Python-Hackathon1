# - Prompts a user to enter their age.
age = int(input("Enter your age: "))
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."
if age >= 18:
    print("You are eligible to vote.")
elif age < 0:
    print("Age can not be negative")    
else:
    print("You are not eligible to vote.")    