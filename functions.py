"""
Functions & Fibonacci Sequence
Question:
Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
"""


def fibonacci(n: int):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        An integer.
    """
    if n <= 1:
        # Complete here
        return n

    # else compute value
    a, b = 1, 1  # complete here
    for _ in range(2, n + 1):
        # Complete here
        a, b = b, a + b
    return b  # add the variable to be returned


if __name__ == "__main__":

    # Get the number of terms from the user
    num_terms = int(input("Enter the number of terms: "))

    # Generate the Fibonacci sequence
    fibonacci_sequence = [fibonacci(i) for i in range(num_terms)]

    # Print the Fibonacci sequence
    print(fibonacci_sequence)


# Your program should:

# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.
