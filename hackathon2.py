def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initializes the sequence with the first two terms

    # Generates the Fibonacci sequence up to the specified term n
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence[:n]  # Return the first n terms of the Fibonacci sequence

# Asking the user to input the value of n
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Generates and prints the Fibonacci sequence
fib_sequence = generate_fibonacci(n)
print("Fibonacci Sequence up to term", n, ":", fib_sequence)
