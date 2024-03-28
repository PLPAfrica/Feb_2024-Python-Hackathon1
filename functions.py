def fibonacci(n):

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  if n <= 1:
    return [n]
  else:
    a, b = 0, 1
    fibonacci_sequence = [a, b]
    for _ in range(2, n + 1):
      c = a + b
      fibonacci_sequence.append(c)
      a, b = b, c
    return fibonacci_sequence  # add the variable to be returned

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = [] 
    if n <= 0:
        return fibonacci_sequence  
    elif n == 1:
        fibonacci_sequence.append(0)  
    else:
        fibonacci_sequence.extend([0, 1])  # If n is greater than 1, add the first two terms (0 and 1) to the sequence
        a, b = 0, 1  
        for _ in range(2, n):
            c = a + b  
            fibonacci_sequence.append(c)  
            a, b = b, c  
    return fibonacci_sequence

  # Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence
