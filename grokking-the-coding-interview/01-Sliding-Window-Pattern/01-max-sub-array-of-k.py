def maxSubArrayofSizeK(arr, k):
    if not arr:
        return 0
    largest, curr = 0, 0
    start = 0

    for end in range(len(arr)):
        curr += arr[end]

        if curr > largest:
            largest = curr

        if end >= k-1:
            curr -= arr[start]
            start += 1

    return largest


array1 = [2, 1, 5, 1, 3, 2]
result1 = maxSubArrayofSizeK(array1, 3)
print(result1)

# After looking at solution notes:
# Could have used max() to compare largest and curr instead of if statement
# otherwise its the same solution


def maxSubArrayofSizeKUpdated(arr, k):
    if not arr:
        return 0
    largest, curr = 0, 0
    start = 0

    for end in range(len(arr)):
        curr += arr[end]

        if end >= k-1:
            largest = max(largest, curr)
            curr -= arr[start]
            start += 1

    return largest

# Complexity
# Time: O(n)
# Space: O(1)
