def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = [] 
    if n <= 0:
        return fibonacci_sequence  
    elif n == 1:
        fibonacci_sequence.append(0)  
    else:
        fibonacci_sequence.extend([0, 1])  # If n is greater than 1, add the first two terms (0 and 1) to the sequence
        a, b = 0, 1  
        for _ in range(2, n):
            c = a + b  
            fibonacci_sequence.append(c)  
            a, b = b, c  
    return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print("Fibonacci sequence up to term", num_terms, ":", fibonacci_sequence)
