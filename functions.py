# Functions & Fibonacci Sequence
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
# Your program should:
# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.

def fibonacci(n):  #Fibonacci sequence is a series of numbers where each number is the sum of the two preceding one, usually starting with 0 and 1. This line defines a function named fibonacci that takes one parameter "n".
  if n <= 1:  #This condition is important because if "n" is less than or equal to 1, the Fibonacci sequence would only contain one or zero elements.
    return [0] if n==1 else [] #If n==1, it returns a list containing only the first Fibonacci number, which is 0. If n is 0 or negative, it returns an empty list because there are no Fibonacci numbers to generate in this case.
  else:    #If "n" is greater than 1, meaning it needs to generate more than one Fibonacci number, the program enters the else block.
    a, b = 0, 1 #Here, a is initialized to 0 and b to 1. These are the first two numbers of the Fibonacci sequence.
    fib_sequence = [a,b]  #We initialize fib_sequence as a list containing the first two Fibonacci sequence.
    for _ in range(2, n + 1):  #This loop iterates from the third Fibonacci number (index 2) up to the nth Fibonacci number (inclusive)
      c = a + b #We calculate the next Fibonacci number by adding the last two Fibonacci numbers, "a" and "b".
      fib_sequence.append(c) #We append the calculated Fibonacci number "c" to the fib_sequence
      a, b = b, c #We update "a" and "b" for the next iteration. "a" becomes "b" and "b" becomes "c".
    return fib_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = [fibonacci(i) for i in range(num_terms)] #Using list comprehension, the code generates the Fibonacci sequence for each index up to num_terms.
# Print the Fibonacci sequence
print(fibonacci_sequence)