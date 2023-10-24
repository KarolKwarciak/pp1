num_fibonacci = 20

fibonacci_sequence = [0, 1]

for i in range(2, num_fibonacci):
    next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_fibonacci)

print(f"Fibonacci sequence of {num_fibonacci} numbers:")
print(fibonacci_sequence)