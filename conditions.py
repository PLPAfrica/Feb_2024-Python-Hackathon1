# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:
def eligibilty(age):
    # - Uses a conditional statement to check if the age is greater than or equal to 18.

    if age >= 18:
        return "You are eligible to vote"
    else:
        return "You are not eligible to vote"


# - Prompts a user to enter their age.
age = int(input("Enter your age: "))

# check if eligible
checkEligibility = eligibilty(age)

# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."
print(checkEligibility)





