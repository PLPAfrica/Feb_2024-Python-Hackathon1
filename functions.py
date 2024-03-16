# Functions & Fibonacci Sequence
def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = []  # Initialize an empty list to store Fibonacci sequence
    if n <= 0:
        return fibonacci_sequence  # Return an empty list if n is non-positive
    elif n == 1:
        return [0]  # Return [0] if n is 1
    else:
        a, b = 0, 1  # Initialize with the first two terms
        fibonacci_sequence = [a, b]  # Store the first two terms
        for _ in range(2, n):
            c = a + b
            a, b = b, c  # Update variables for the next iteration
            fibonacci_sequence.append(c)
        return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print("Generated Fibonacci sequence:", fibonacci_sequence)
