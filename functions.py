def fibonacci(n) :
    if n <=1:
      return (0)
    else:
       a, b = 0, 1
       for _ in range(2, n+1):
          c=a+b
          a, b = b, c
          return [0, 1] + [c]
 #Get the number of trms from user      
num_terms = int(input("Enter the number of terms: "))

#Generate the fibbonacci sequence
fibonacci_sequence = fibonacci(num_terms)

#Print the fibonacci sequence
print("The Fibonacci sequence is:")
print(fibonacci_sequence)