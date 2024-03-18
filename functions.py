# Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the first n terms of the Fibonacci sequence.
  """
  if n <= 1:
    return n
  else:
    # Initialize the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]
    # Generate the remaining terms using a loop
    for i in range(2, n + 1):
      next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
      fibonacci_sequence.append(next_term)
    return fibonacci_sequence

# Get user input for the number of terms
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Generate and print the Fibonacci sequence
fibonacci_sequence = fibonacci(n)
print("Fibonacci sequence up to", n, "terms:")
print(fibonacci_sequence)

# Your program should:

# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.

