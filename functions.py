# Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  fibonacci_sequence = [0,1]
  if n <= 1:
    return fibonacci_sequence[:n + 1]
  else:
    a, b = 0, 1
    for _ in range(2, n + 1):
      c = a + b
      fibonacci_sequence.append(c)
      a,b = b, c
    return fibonacci_sequence

def main():
    num_terms = int(input("Enter the number of terms: "))
    fibonacci_sequence = fibonacci(num_terms)
    print("The Fibbonacci sequence up to term", num_terms, "is:")
    print(fibonacci_sequence)

if __name__ == "__main__":
  main()

