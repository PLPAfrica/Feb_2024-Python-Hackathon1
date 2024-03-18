
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.

# Functions & Fibonacci Sequence
def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  if n <= 1:
    return n         # Base case: return 0 or 1 for n <= 1  # Completed here
  else:
    a, b = 0, 1      # Initialize first two Fibonacci numbers  # Completed here
    for _ in range(2, n + 1):
      c = a + b
      a = b           # Updated a for the next iteration  # Completed here
      b = c           # Updated b for the next iteration   # Completed here
    return c          # added the variable to be returned - Return the last calculated term

# Ask the user to input the value of n.
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = []
for i in range(num_terms):
  fibonacci_sequence.append(fibonacci(i))

# Print the Fibonacci sequence
print(fibonacci_sequence)








# Your program should:

# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.

