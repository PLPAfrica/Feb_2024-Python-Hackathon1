def Fibonacci(n):
  if n < 0:
    raise ValueError("Please enter a non-negative number")
  elif n == 0:
    return []
  elif n == 1:
    return [0]

  my_fibonacci_list = [0, 1]
  while len(my_fibonacci_list) < n:
    number = my_fibonacci_list[-1] + my_fibonacci_list[-2]
    my_fibonacci_list.append(number)
  return my_fibonacci_list


number = int(input('Please enter a number: '))
try:
  print (f"Here is the Fibonacci sequence of the first {number} term(s): {Fibonacci(number)}")
except ValueError as e:
  print(e)