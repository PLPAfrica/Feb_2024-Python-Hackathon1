

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Main program to get user input and print Fibonacci sequence
def main():
    n = int(input("Enter the number of terms for Fibonacci sequence: "))
    fibonacci_sequence = generate_fibonacci(n)

    print("Fibonacci sequence up to term", n, ":", fibonacci_sequence)

