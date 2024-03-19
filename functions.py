def generate_fibonacci(n):
    """
    Generate the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = []  # Initialize an empty list to store the Fibonacci sequence

    if n <= 0:
        return fibonacci_sequence  # Return an empty sequence if n is non-positive
    elif n == 1:
        fibonacci_sequence = [0]  # If n is 1, Fibonacci sequence is [0]
    else:
        a, b = 0, 1  # Initialize the first two terms of the Fibonacci sequence
        fibonacci_sequence = [a, b]  # Start the sequence with the initial terms

        for _ in range(2, n):
            c = a + b  # Calculate the next Fibonacci number
            fibonacci_sequence.append(c)  # Append the next Fibonacci number to the sequence
            a, b = b, c  # Update the values of a and b for the next iteration

    return fibonacci_sequence


# Get the number of terms from the user with error checking
while True:
    try:
        num_terms = int(input("Enter the number of terms (a positive integer): "))
        if num_terms <= 0:
            raise ValueError("Please enter a positive integer.")
        break  # Exit the loop if input is valid
    except ValueError as ve:
        print(ve)

# Generate the Fibonacci sequence using the iterative approach
fibonacci_sequence = generate_fibonacci(num_terms)

# Print the Fibonacci sequence
print("Fibonacci sequence:", fibonacci_sequence)
