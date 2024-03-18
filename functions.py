def fibonacci_sequence(n):
    sequence = [0,1]# initializimg the first two terms of the fibonacci sequence

    # Generating the sequence to the nth term
    for i in range (2, n):
        sequence = sequence.append(sequence[-1] + sequence[-2])

    return sequence

def main():
    number = int(input("Enter a number: "))#user input for the number
    sequence = fibonacci_sequence(number)# using the input to generate the sequence

    # output of the Fibonacci sequence generated
    print(f"Sequence: \n{sequence}")

if __name__ == "__main__":
    main()