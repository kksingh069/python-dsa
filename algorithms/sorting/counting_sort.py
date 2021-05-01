"""
High level description:

Time complexity:

"""

def counting_sort(arr):
    # Find min and max values
    min_value = min(arr)
    max_value = max(arr)

    counting_arr = [0]*(max_value-min_value+1)
    for num in arr:
        counting_arr[num-min_value] += 1
    
    index = 0
    for i, count in enumerate(counting_arr):
        for _ in range(count):
            arr[index] = min_value + i
            index += 1

test_array = [3, 3, 2, 6, 4, 7, 9, 7, 8]

counting_sort(test_array)

print(test_array)
