# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

age = int(input('Enter your age: '))

while True:
    if 150 >= age >= 18:
        print(f'{age} is an eligible age to vote')
    elif 18 > age >=0:
        print(f'{age} is too young to vote, not eligible')
    else:
        print('Enter a valid age!')
    break