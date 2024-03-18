def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fib_sequence = []  # List to store the Fibonacci sequence
    if n <= 0:
        return fib_sequence  # Return an empty list if n is 0 or negative
    elif n == 1:
        fib_sequence.append(0)  # First term of Fibonacci sequence
    else:
        fib_sequence.extend([0, 1])  # Initial terms of Fibonacci sequence
        a, b = 0, 1  # Initial values for Fibonacci calculation
        for _ in range(2, n):
            c = a + b
            fib_sequence.append(c)  # Add the next term to the sequence
            a, b = b, c  # Update values for next iteration
    return fib_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)
