def fibonacci(n):

    fib_sequence = []
    if n <= 0:
        return fib_sequence
    elif n==1:
        fib_sequence.append(0)
        return fib_sequence
    else:
        fib_sequence = [0,1]
        a, b = 0,1
        for _ in range(2, n + 1):
            c = a + b
            fib_sequence.append(c)
            a, b = b, c
        return fib_sequence

num_terms = int(input("Enter the number of terms: "))

fibonacci_sequence = fibonacci(num_terms)

print("Fibonacci sequence: ")
for term in fibonacci_sequence:
    print(term, end=" ")    
