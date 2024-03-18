def fibonacci(n):
    
    fibonacci_sequence = []  

    if n <= 1:
        fibonacci_sequence = [0] if n == 0 else [0, 1]  
    else:
        a, b = 0, 1  
        fibonacci_sequence = [a, b]  
        for _ in range(2, n): 
            c = a + b  
            fibonacci_sequence.append(c) 
            a, b = b, c  

    return fibonacci_sequence  

num_terms = 15

fibonacci_sequence = fibonacci(num_terms)

print("Generated Fibonacci sequence:", fibonacci_sequence)