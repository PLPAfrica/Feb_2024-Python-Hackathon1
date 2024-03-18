# Functions & Fibonacci Sequence

#Create a function
def fibonacci(n):
    
    if n <= 1: 
        exit #Break out of the iteration loop.           
    else:
        #Initialize the first two terms of the sequence.
        a, b = 0, 1
    for _ in range(2, n+1): #Range with start : 2 and stop : n+1 
      c = a + b
      a, b = b, c
      n = c #Assign the value of c to n
    return n

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Initialize list
fibonacci_sequence = []

#for loop to iterate through the number of terms
for i in range(num_terms):
  # Call the function and pass the number of terms as an argument
  fibonacci_sequence.append(fibonacci(i))
  

# Print the Fibonacci sequence
print(fibonacci_sequence)


# Your program should:

# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.
