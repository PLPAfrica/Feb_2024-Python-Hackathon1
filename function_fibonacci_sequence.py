def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fib_sequence = []
    if n <= 1:
        fib_sequence = [0] if n == 1 else []
    else:
        a, b = 0, 1
        fib_sequence = [a, b]
        for _ in range(2, n):
            c = a + b
            fib_sequence.append(c)
            a, b = b, c
    return fib_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print("Fibonacci sequence up to the", num_terms, "th term:", fibonacci_sequence)
