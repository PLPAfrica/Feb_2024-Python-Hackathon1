def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence[:n]

try:
    # Task 1: Fibonacci Sequence
    n = int(input("Enter the value of n for the Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_sequence = generate_fibonacci(n)
        print("Fibonacci sequence:", fibonacci_sequence)

    # Task 2: Voting Eligibility
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

except ValueError:
    print("Invalid input. Please enter a valid integer for Fibonacci sequence and a valid age for voting eligibility.")
