# Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n using iteration.
  
  Args:
      n: The number of terms in the Fibonacci sequence.
  
  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  fibonacci_sequence=[]
  if n <= 1:
    return [n]
  else:
    a, b = [0,1]
    for _ in range(2, n):
      c = a + b
      a,b= b,c
      fibonacci_sequence.append(c)
  return fibonacci_sequence
num_terms = int(input("Enter the number of terms: "))


# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)


# Your program should:

# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.

