def min_swaps(arr, k):
    count = 0
    for i in arr:
        if i <= k:
            count += 1

    bad = 0
    for i in range(0, count):
        if arr[i] > k:
            bad += 1

    ans = bad
    j = count

    for i in range(0, len(arr)):
        if j == len(arr):
            break

        if arr[i] > k:
            bad -= 1  
        
        if arr[j] > k:
            bad += 1

        ans = min(bad, ans)
        j += 1

    print('answer - ', ans)

arr = [2,7,9,5,8,7,4]
min_swaps(arr, 5)
