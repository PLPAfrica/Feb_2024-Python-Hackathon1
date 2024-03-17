# Python program for Conditional Statement with input validation

while True:
    try:
        age = int(input("Enter your age: "))
        if 1 <= age <= 130:
            break  # Exit the loop if age is within the valid range
        else:
            print("Age must be between 1 and 130")
    except ValueError:
        print("Please enter a valid age")

# Check eligibility to vote
print("You are eligible to vote") if age >= 18 else print("You are not eligible to vote")
