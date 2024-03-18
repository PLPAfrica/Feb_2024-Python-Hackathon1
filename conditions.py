# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."
def check_voting_eligibility():
  """Prompts the user for their age and determines eligibility to vote."""
  try:
    age = int(input("Enter your age: "))
    if age >= 18:
      print("You are eligible to vote.")
    else:
      print("You are not eligible to vote.")
  except ValueError:
    print("Please enter a valid age (integer).")

check_voting_eligibility()