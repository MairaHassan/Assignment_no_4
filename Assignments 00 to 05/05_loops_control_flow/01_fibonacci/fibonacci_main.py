from fibonacci_utils import MAX_VALUE, generate_fibonacci_up_to

fib_sequence = generate_fibonacci_up_to(MAX_VALUE)

for num in fib_sequence:
    print(num, end=' ')
print()  # for newline
