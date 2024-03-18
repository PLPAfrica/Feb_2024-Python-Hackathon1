# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:
def main():
    # -Prompts the user to enter their age
    age = int(input("Enter your age: "))
    # - Uses a conditional statement to check if the age is greater than or equal to 18.
    if age >= 18:
        # - Prints "You are eligible to vote" if true, "
        print("You are eligible to vote")
    else:
        # - otherwise "You are not eligible to vote.
        print("You are not eligible to vote")

if __name__ == "__main__":
    main()
