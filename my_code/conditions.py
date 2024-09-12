#
#* Create a Python program that:

#~ - Prompts a user to enter their age.
#~ - Uses a conditional statement to check if the age is greater than or equal to 18.
#~ - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

# Prompt the user to enter their age
# age = int(input("Enter your age: "))

# # Check if the age is greater than or equal to 18
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

def check_voting_eligibility(age):
    """
    This function checks if the given age is eligible for voting.

    Args:
        age (int): The age of the user.

    Returns:
        str: A message indicating whether the user is eligible to vote or not.
    """
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

def main():
    # Prompt the user to enter their age
    age = int(input("Enter your age: "))

    # Check voting eligibility using the function
    message = check_voting_eligibility(age)

    # Print the result
    print(message)

# Call the main function to execute the program
if __name__ == "__main__":
    main()

