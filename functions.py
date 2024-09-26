def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for _ in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence

n = int(input("Enter the number of terms: "))
fibonacci_sequence = generate_fibonacci(n)
print(fibonacci_sequence)
