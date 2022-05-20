# Given a string, find the length of the longest substring in it with no more than K distinct characters.


def maxSubstringOfKUnique(s, k):
    longest, start = 0, 1
    substr = ""
    print(s)

    for end in range(len(s)):
        substr += s[end]
        uniques = len(set(substr))

        if longest < len(substr) and uniques <= k:
            longest = len(substr)

        while uniques > k:
            # mistake here substr[start:] vs substr[1:]
            substr = substr[1:]
            uniques = len(set(substr))
            start += 1

    return longest


s1 = "araaci"
r1 = maxSubstringOfKUnique(s1, 2)
print(f"r1: {r1}")

s2 = "cbbebi"
r2 = maxSubstringOfKUnique(s2, 3)
print(f"r2: {r2}")

# Notes
'''
- The solution given uses a dictionary to count the occurrences of each letter and the amount of distinct letter so far
- Its the same solution though, I just used a 'set' instead which creates only includes each unique letter once 
    - Space complexity does change with a set, it is O(n) space complexity vs O(k) with a hash map/dictionary
- Mistakes with arrays and counting from the wrong spot can cost you time and brain power debugging,
'''
