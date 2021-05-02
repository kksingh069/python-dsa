def find(arr):
    if len(arr) == 1:
        return arr[0]

    count_negative = 0
    count_zero = 0
    max_neg = float('-inf')
    min_pos = float('inf')

    prod = 1

    for num in arr:
        if num == 0:
            count_zero += 1
            continue

        if num < 0:
            count_negative += 1
            max_neg = max(max_neg, num)

        if num > 0:
            min_pos = min(min_pos, num)

        prod *= num

    if count_zero == len(arr) or (count_negative == 0 and count_zero > 0):
        return 0

    if count_negative == 0:
        return min_pos

    if count_negative & 1 == 0 and count_negative != 0:
        prod = int(prod / max_neg)

    return prod
