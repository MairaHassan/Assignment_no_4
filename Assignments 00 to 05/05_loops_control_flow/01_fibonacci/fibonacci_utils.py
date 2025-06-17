MAX_VALUE = 10000

def generate_fibonacci_up_to(limit):
    sequence = []
    a, b = 0, 1
    while a < limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence
