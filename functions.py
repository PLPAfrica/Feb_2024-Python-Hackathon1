def generate_fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth term.

    Parameters:
        n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
        list: A list containing the first n terms of the Fibonacci sequence.
    """
    fibonacci_sequence = [0, 1]
    if n <= 2:
        return fibonacci_sequence[:n]
    else:
        for i in range(2, n):
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
        return fibonacci_sequence

def main():
    n = int(input("Enter a number  "))
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci sequence for :")
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()
