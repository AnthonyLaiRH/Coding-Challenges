# Given an array of positive numbers and a positive number 'k'
# Find the smallest contiguous subarray with sum greater than or equal to 'k'
# return 0 if no such array exists

# Pseudocode
'''
start = 0
sum = 0
shortest = 0
for end in len(a)

'''


def smallestSubArrayWithSum(a, k):
    start, total = 0, 0
    shortest = len(a) + 1
    for end in range(len(a)):
        total += a[end]

        while total >= k:
            windowSize = end - start + 1
            if windowSize < shortest:
                shortest = windowSize
            if shortest == 1:
                return shortest
            total -= a[start]
            start += 1
    return 0 if shortest == len(a) + 1 else shortest


a1 = [2, 1, 5, 2, 3, 2]
r1 = smallestSubArrayWithSum(a1, 7)
print(f'a1: {a1} r1: {r1}')

a2 = [2, 1, 5, 2, 8]
r2 = smallestSubArrayWithSum(a2, 7)
print(f'a2: {a2} r2: {r2}')

# Aftermath Notes:
'''
 - correct use of the loop (was the second idea so remember about this use of it)
 - can use math.inf instead of len(a) + 1, even though len(a)+1 is impossible in the problem, it just looks nicer
 - use min() to get rid of some of the if statements for cleaner code
 - the ternary at the end is actually fine, or use if statement if you want to be more verbose
'''

# Complexity:
# Time: O(n)
# Space: O(1)

# With min() and math.inf


def smallestSubArrayWithSumV2(a, k):
    start, total = 0, 0
    shortest = math.inf
    for end in range(len(a)):
        total += a[end]

        while total >= k:
            shortest = min(shortest, end - start + 1)
            total -= a[start]
            start += 1
    return 0 if shortest == math.inf else shortest


a3 = [2, 1, 5, 2, 3, 2]
r3 = smallestSubArrayWithSum(a3, 7)
print(f'a3: {a3} r3: {r3}')

a4 = [2, 1, 5, 2, 8]
r4 = smallestSubArrayWithSum(a4, 7)
print(f'a4: {a4} r4: {r4}')
