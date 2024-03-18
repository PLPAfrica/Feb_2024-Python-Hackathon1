# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

# Define a function called main
def main():
    # Prompt the user to enter their age and store it in a variable called age
    age = int(input("Please enter your age: "))

    # Check if the age is greater than or equal to 18
    if age >= 18:
        # If the condition is True, print "You are eligible to vote"
        print("You are eligible to vote.")
    else:
        # If the condition is False, print "You are not eligible to vote."
        print("You are not eligible to vote.")

# Check if the script is being run directly
if __name__ == "__main__":
    # If it is, call the main function
    main()

