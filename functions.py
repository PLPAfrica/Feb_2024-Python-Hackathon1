def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  if n < 0:
    print('List of items should be greater than one')
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    a, b = 0, 1
    for i in range(2, n + 1):
      c = a + b
      a, b = b, c
    return b

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = []
if num_terms != 0:
  for i in range(num_terms):
    # Print the Fibonacci sequence
    fibonacci_sequence.append(fibonacci(i))
print(fibonacci_sequence)

