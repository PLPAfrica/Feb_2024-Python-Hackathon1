def generate_fibonacci(n):
    fibonacci_seq = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_term)
    return fibonacci_seq[:n]

def main():
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci sequence up to term", n, ":", fibonacci_sequence)

if __name__ == "__main__":
    main()
