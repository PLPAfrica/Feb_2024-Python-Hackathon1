# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

def check_voting_eligibility(age):
    """
    Check if the given age is eligible for voting.

    Args:
        age: The age of the person.

    Returns:
        A message indicating whether the person is eligible to vote or not.
    """
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

def main():
    try:
        # Prompt the user to enter their age
        age = int(input("Please enter your age: "))
        print(check_voting_eligibility(age))
    except ValueError:
        print("Invalid input. Please enter a valid age as a whole number.")

if __name__ == "__main__":
    main()

