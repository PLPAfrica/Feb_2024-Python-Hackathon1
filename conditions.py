# Python program for Conditional Statement with input validation

# Continuously prompt the user to enter their age until a valid age is provided
while True:
    try:
        age = int(input("Enter your age: "))  # Get user input for age
        if 1 <= age <= 130:  # Check if age is within the valid range
            break  # Exit the loop if age is within the valid range
        else:
            print("Age must be between 1 and 130.")  # Print error message for age out of range
    except ValueError:
        print("Please enter a valid age.")  # Print error message for invalid age input

# Check eligibility to vote based on the provided age
print("You are eligible to vote.") if age >= 18 else print("You are not eligible to vote.")
