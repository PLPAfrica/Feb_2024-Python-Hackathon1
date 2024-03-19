def fibonacci(n):
 """Generates the Fibonacci sequence up to a specified term n."""

 if n <= 1:
   return n
 else:
   # Optimized for clarity using a list to store terms
   fib_sequence = [0, 1]
   for i in range(2, n + 1):
     next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
     fib_sequence.append(next_term)
   return fib_sequence

# Get user input for the number of terms
n = int(input("Enter the number of terms: "))

# Generate and print the Fibonacci sequence
fibonacci_sequence = fibonacci(n)
print("Fibonacci sequence:", fibonacci_sequence)
