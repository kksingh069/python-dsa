def is_perfect_square(num):
    """


    """
    i = 0
    while i * i < num:
        i += 1
    if i * i == num:
        return True
    else:
        return False
        

# Test
print(is_perfect_square(16))
print(is_perfect_square(14))
