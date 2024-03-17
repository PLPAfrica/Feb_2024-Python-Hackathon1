# Python Conditional Statements


# Create a Python program that:
class VoterEligibility:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."
    def check_age(self):
        if self.age >= 18:
            print(f"Hello {self.name}, you are eligible to vote.")
        else:
            print(f"Am sorry {self.name}, you are not eligible to vote.")

# - Prompts a user to enter their name.
name = input("Your name: ")

# - Prompts a user to enter their age.
age = int(input("Your age: "))

voter = VoterEligibility(name, age)

voter.check_age()