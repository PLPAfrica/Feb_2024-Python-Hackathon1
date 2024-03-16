def fibonacci_sequence(n):
    # Initialize the sequence with the first two terms
    sequence = [0, 1]

    # Generate subsequent terms
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

def main():
    # Ask the user to input the value of n
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))

    # Generate the Fibonacci sequence
    sequence = fibonacci_sequence(n)

    # Print the generated Fibonacci sequence
    print("Fibonacci sequence up to term", n, ":", sequence)

if __name__ == "__main__":
    main()
