# 
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
"""
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
#   program

def fibonacci(n):
    if n <= 1:
        return [0] if n == 1 else []
    else:
        a, b = 0, 1
        fibonacci_sequence = [a, b]
        for _ in range(2, n):
            c = a + b
            fibonacci_sequence.append(c)
            a, b = b, c
        return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print("Fibonacci sequence up to term", num_terms, ":", fibonacci_sequence)






# def generate_fibonacci(n):
#     fibonacci_sequence = [0, 1]
#     while len(fibonacci_sequence) < n:
#         next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
#         fibonacci_sequence.append(next_term)
#     return fibonacci_sequence[:n]

# # Test the function
# n = int(input("Enter the number of terms for Fibonacci sequence: "))
# fibonacci_sequence = generate_fibonacci(n)
# print("Fibonacci sequence up to term", n, ":", fibonacci_sequence)
