import datetime

# Prompt the user to enter their birth year
birth_year = int(input("In what year were you born? "))

# Calculate the user's age
current_year = datetime.datetime.now().year
age = current_year - birth_year

# Check if the user is eligible to vote
if age >= 18:
    print("Congratulations! You have earned the right to shape the future with your vote.")
    print("Use this power wisely, for the fate of nations rests upon your decision.")
else:
    remaining_years = 18 - age
    print(f"Patience, young one. Your time to influence the world's destiny will come in {remaining_years} years.")
    print("Until then, continue to grow in wisdom and understanding.")
