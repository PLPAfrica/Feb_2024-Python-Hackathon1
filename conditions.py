# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

print("Hello, citizen, welcome to our age checker")

age = input("Enter your age: ")
try:
    agE = int(age)
except ValueError:
    print("Invalid output. Try an integer")
    
def voter_ager():
    if (agE >= 18):
        print("You are eligible to vote. Make the right choice!")
    else:
        print("You are not allowed to vote, try again when of legal age!")
    


voter_ager()
