# Python program for Fibonacci sequence with input validation

def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    # Initialize an empty list to store Fibonacci sequence
    fibonacci_sequence = [] 
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1  
    
    # Return an empty list for non-positive n
    if n <= 0:
        return fibonacci_sequence 
    
    # Append the first Fibonacci number for n = 1
    elif n == 1:
        fibonacci_sequence.append(a)  
        return fibonacci_sequence
      
    # Append the first two Fibonacci numbers for n >= 2
    else:
        fibonacci_sequence.extend([a, b]) 
        
        for number in range(2, n):
            c = a + b  # Calculate the next Fibonacci number
            a, b = b, c  # Update a and b for the next iteration
            fibonacci_sequence.append(c)  # Append the next Fibonacci number to the sequence
            
        return fibonacci_sequence

# Continue prompting user for the number of terms until the user quits
while True:
  
    # Exit the loop if the user types 'quit'
    num_terms_input = input("Enter the number of terms or type 'done' to exit: ")
    
    if num_terms_input.lower() == 'done':
        break  
      
    try:
        num_terms = int(num_terms_input)  # Convert user input to an integer
        if num_terms > 0:  # Check if input is a positive integer
            # Generate the Fibonacci sequence
            fibonacci_sequence = fibonacci(num_terms)
            # Print the Fibonacci sequence
            print(fibonacci_sequence)
            
        else:
          # Prompt user to enter a positive integer
            print("Please enter a positive number.")  
            
          # Prompt user to enter a valid integer
    except ValueError:
        print("Please enter a valid integer or type 'quit' to exit.")
