def fibonacci(n):
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    
    return fib_sequence[:n]

# Example: Print the first 10 Fibonacci numbers
n = 12

result = fibonacci(n)
print(result)
