# Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
# Your program should:
  # Ask the user to input the value of n.
  # Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
  # Print the generated Fibonacci sequence.
  
  
def generate_fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fibonacci = [0, 1]
        for i in range(2, n):
            next_term = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(next_term)
        return fibonacci


# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = generate_fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)

