def fibonacci (n, memo= {}):
    if n in memo:
      return memo[n]

    if n <=1 :
      return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci (n-2, memo)
    return memo[n]

def fibonacci_sequence (n):
   sequence = [fibonacci(i) for i in range (n)]
   return sequence

def main():
    try:
        n = int(input("Enter the number of Fibonacci numbers to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        print(f"Fibonacci sequence: {fibonacci_sequence(n)}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

