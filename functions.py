def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = []
    if n <= 1:
        fibonacci_sequence.extend([0, 1][:n+1])  
    else:
        a, b = 0, 1
        fibonacci_sequence.extend([a, b])  
        for _ in range(2, n):
            c = a + b
            fibonacci_sequence.append(c)
            a, b = b, c
    return fibonacci_sequence


num_terms = int(input("Enter the number of terms: "))

fibonacci_sequence = fibonacci(num_terms)

print(fibonacci_sequence)
