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
        fibonacci_sequence.append(0)
    elif n == 1:
        fibonacci_sequence.extend([0, 1]) 
    else:
        a, b = 0, 1  
        fibonacci_sequence.extend([a, b])  
        for _ in range(2, n):
            c = a + b
            fibonacci_sequence.append(c)  # Add the next term to the sequence
            a, b = b, c  # Update variables for the next iteration
    return fibonacci_sequence



userInputs = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(userInputs)

# Prints out  the Fibonacci sequence
print(fibonacci_sequence)
