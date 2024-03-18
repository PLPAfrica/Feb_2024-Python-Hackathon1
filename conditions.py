# Python Conditional Statements 

# Python program:

# defined the main() function
def main():
    
      # defines a variable voting_age to represent the minimum age for votin
    voting_age = 18

      #1 Prompt user to enter their age
    age = int(input("Enter your age: "))

      #Check if eligible to vote
      #2 Uses a conditional statement to check if the age is greater than or equal to 18.
    if age >= voting_age:
         # If it is, the program prints a message indicating eligibility
        print("You are eligible to vote.")
    else:
         # otherwise, it prints a message indicating ineligibility.
        print("You are not eligible to vote.")
  
if __name__ == "__main__":
    main()
                # if __name__ == "__main__": checks if the script is being run as the main program. If true, it executes the block of code inside the if statement. If false, it means the script is being imported as a module, and the block of code is not executed.






# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

# Changes Made:

# Created a Python program to check voting eligibility based on age input.
# Implemented a conditional statement to determine eligibility.
# I added comments for clarity and documentation.
# This pull request fulfills the requirements of the task