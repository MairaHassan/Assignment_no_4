def double_until_limit(curr_value):
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ')
    print()  # For newline after the loop
