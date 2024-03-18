
print("Welcome")
age=int(input("Enter your age "))
if(age>=18):
    print(f"You are {age} years old: ", end='')
    print("You are eligible to vote ")
else:
    print(f"You are {age} years old:",end='')
    print("You are not eligible to vote ")