# This function has the age question
def question():
    return int(input("\nHow old are you: "))

#Checks for eligibility
def check_age(age):
    if age < 18:
        print("You are not eligible to vote\n")
    else:
        print("You are eliglible to vote\n")

# main function
def main():
    age = question()
    if age < 0:
        print("The age you entered is invalid")
        question()
    else:
        check_age(age)

if __name__ == "__main__":
    main()