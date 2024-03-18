#asking user for input
n=int(input("Enter the maximum term you desire your sequence to reach"))
#function  to generate the fibonnacci sequence
def fibonacci_sequence(n):
    fibonachi_Values=[0,1]
   #use of while to check condition before generating sequence 
    while(fibonachi_Values[-1] + fibonachi_Values[-2] <=n):
      next_value=fibonachi_Values[-1] + fibonachi_Values[-2]
      fibonachi_Values.append(next_value)
    
    return fibonachi_Values
#calling  the function
fib_sequence=fibonacci_sequence(n)
print(f"The fibonnacci sequence generated upto {n} is  {fib_sequence}")