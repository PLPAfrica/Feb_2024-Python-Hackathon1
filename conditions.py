#ask to enter age
age= int(input("Enter your age:"))
#initialize result variable
result=""
#check if status
if age>=18:
    result="You are eligible to vote"
elif age<18:
    result="You are not eligible to vote"
#print the result
print(result)    
    
