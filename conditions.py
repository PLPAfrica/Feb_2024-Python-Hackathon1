# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."
age = int(input('Enter your age: '))
if age >= 18:
    #if the condition is True, this line of code will run
    print(f'Since your age is {age} years, hence, You are eligible to vote ')

else:
    #if the condition is False, this line of code will run
    print("You're not eligible to vote")
    