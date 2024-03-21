#Code to check wheteher a user is eligible to vote or not.
while True:
    age = int(input("Enter your age or 0 to exit: "))
    name = input("Enter your name: ")
    if age == 0:
        break
    elif age >= 18:
        print(f"\nDear {name} You are eligible to vote.\nPlease vote wisely.\n")
    else:
        print("\nSorry {} You are not eligible to vote.".format(name))
        print("You can vote after {} years.".format(18 - age))
        quit = input("Do you want to continue? (y/n): ")
        if quit == 'y' or quit == 'Y':
            break
        else:
            continue