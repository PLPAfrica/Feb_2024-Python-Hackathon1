def main():
    """
    Prompts the user to enter their age and checks eligibility to vote.

    This function prompts the user to enter their age, then checks whether the
    age entered is greater than or equal to 18. Depending on the result, it prints
    either "You are eligible to vote" or "You are not eligible to vote".
    """
    # Prompt the user to enter their age
    age = int(input("Please enter your age: "))

    # Check if the age is greater than or equal to 18
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

if __name__ == "__main__":
    main()
