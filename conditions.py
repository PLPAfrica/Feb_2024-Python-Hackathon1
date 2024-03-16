# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."
import random

def check_voting_eligibility(age):
    """
    This function checks if the user is eligible to vote based on their age.

    Args:
        age: The age of the user.

    Returns:
        A string indicating the voting eligibility status.
    """
    if age >= 18:
        return "You are eligible to vote! 🗳️"
    else:
        return "You are not eligible to vote. 😔"

def display_encouragement(age):
    """
    This function displays an encouraging message based on the user's age.

    Args:
        age: The age of the user.
    """
    if age >= 18:
        encouragement_messages = [
            "Every voice matters, no matter the age. Keep striving for positive change!",
            "Your time will come! Don't lose hope.",
            "Even if you can't vote yet, there are many ways to contribute to society. Keep shining!"
        ]
        message = random.choice(encouragement_messages)
        print("\n" + "-" * 30)
        print(message)
        print("-" * 30)
        print("\nWhen you will vote, vote wisely. 😊")
    else:
        print("\n" + "-" * 30)
        print("Patience, your time to make a difference will come. 😊")
        print("-" * 30)

def main():
    # Prompt the user to enter their age
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                raise ValueError("Age must be a positive integer.")
            break
        except ValueError:
            print("Invalid input. Age must be a positive integer. Please try again.")

    # Check voting eligibility
    eligibility_status = check_voting_eligibility(age)

    # Print a decorative header
    print("\n" + "=" * 30)
    print("VOTING ELIGIBILITY CHECKER")
    print("=" * 30)

    # Print the result
    print("\n" + "-" * 30)
    print(eligibility_status)
    print("-" * 30)

    # Display an encouraging message based on age
    display_encouragement(age)

if __name__ == "__main__":
    main()
