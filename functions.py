# Function to generate Fibonacci sequence up to specified term n
def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = [0, 1]  # Initialize with first two terms
    
    # Generating Fibonacci sequence
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

# Function to visualize Fibonacci sequence using stars as different shapes
def visualize_fibonacci_shapes(sequence):
    max_value = max(sequence)
    
    # Loop through each Fibonacci term
    for term in sequence:
        # Draw triangle
        print("*" * term)
        
        # Draw square
        print("*" * max_value)
        
        # Draw diamond
        spaces = max_value - term
        print(" " * spaces + "*" * term + " " * spaces)
        
        print()  # Add an empty line between shapes

# Main function
def main():
    # Getting user input for the number of terms
    n = int(input("Enter the number of terms in Fibonacci sequence: "))
    
    # Generate Fibonacci sequence
    fibonacci_sequence = fibonacci(n)
    
    # Visualize Fibonacci sequence using different shapes
    print("Visualizing Fibonacci Sequence using Different Shapes:")
    visualize_fibonacci_shapes(fibonacci_sequence)
    
    # Print the generated Fibonacci sequence
    print("\nGenerated Fibonacci Sequence:")
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()
