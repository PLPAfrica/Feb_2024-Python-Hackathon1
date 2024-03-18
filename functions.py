# # Functions & Fibonacci Sequence
# # Question
# # Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
# #We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
# def fibonacci(n):
#   """
#   This function generates the Fibonacci sequence up to a specified term n using iteration.

#   Args:
#       n: The number of terms in the Fibonacci sequence.

#   Returns:
#       A list containing the Fibonacci sequence up to n terms.
#   """
#   if n <= 1:
#     # Complete here
#   else:
#     a, b = # complete here
#     for _ in range(2, n + 1):
#       c = a + b
#       # Complete here
#     return # add the variable to be returned

# # Get the number of terms from the user
# num_terms = int(input("Enter the number of terms: "))

# # Generate the Fibonacci sequence
# fibonacci_sequence = []
# for i in range(num_terms):
#   fibonacci_sequence.append(fibonacci(i))

# # Print the Fibonacci sequence
# print(fibonacci_sequence)


# # Your program should:

# # Ask the user to input the value of n.
# # Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# # Print the generated Fibonacci sequence.

def fibonacci(n):
    fibonacci_sequence = []  # Initialize an empty list to store the Fibonacci sequence
    
    # Initialize first two terms of Fibonacci sequence
    a = 0
    b = 1
    
    # Loop to generate Fibonacci sequence up to nth term
    for i in range(n):
        fibonacci_sequence.append(a)  # Append current term to the sequence
        
        # Calculate next term in the sequence
        next_term = a + b
        
        # Update values for next iteration
        a = b
        b = next_term
        
    return fibonacci_sequence

# Example usage:
n = int(input("Enter the value of n: "))
fibonacci_sequence = fibonacci(n)
print("Fibonacci sequence up to term", n, ":", fibonacci_sequence)
