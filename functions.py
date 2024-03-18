def generate_fibonacci_sequence(n):
    sequence = [0, 1] #Initialize the sequence with the first two terms

    for i in range(2, n):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)

        return sequence
    
    #Ask the user to input the value of n
    n = int(input("Enter the value of n:"))

    #Create a function to generate the Fibonacci sequenec
    fibonacci_sequence = generate_fibonacci_sequence(n)

    #Print the generated Fibonacci sequence
    print("The Fibonacci sequence up to {n} terms:")
    print(fibonacci_sequence)

