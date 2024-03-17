def generate_fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth term.

    Parameters:
    - n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
    - list: A list containing the first n terms of the Fibonacci sequence.
    """

    # Initialize the sequence with the first two terms
    fibonacci_sequence = [0, 1]
    for i in range(2, n):  # Iterate from the third term onwards
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calculate the next term
        # Add the next term to the sequence
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]  # Return the first n terms of the sequence


def main():
    """
    Main function to execute the program.
    """

    # use input
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))
    if n <= 0:
        # Check if input is valid
        print("Please enter a positive integer.")
    else:
        # Generate Fibonacci sequence
        fibonacci_sequence = generate_fibonacci(n)
        # Print the generated sequence
        print("Fibonacci sequence up to ", n,"term", ":", fibonacci_sequence)


if __name__ == "__main__":
    main()  # Call the main function
