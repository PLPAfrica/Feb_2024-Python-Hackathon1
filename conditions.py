def user_age():
    ''' This program asks for user age and returna message if the user is eligible for voting or not '''
    age = int(input('Enter Your Age'))
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")


user_age()