# Input from the user
n = int(input("Enter the value of n: "))
#Fibonacci Sequence Generation Function
def generate_fibonacci_sequence(n):
    # Initialize the sequence with the first two terms
    fibonacci_sequence = [0, 1]  

    # Generate subsequent in terms of the Fibonacci sequence
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence
# Main Function:
def main():
    # Ask the user to input the value of n
    n = int(input("Enter the value of n: "))

    # Generate the Fibonacci sequence
    fibonacci_sequence = generate_fibonacci_sequence(n)

    # Print the generated Fibonacci sequence
    print("Generated Fibonacci sequence up to term", n, ":", fibonacci_sequence)