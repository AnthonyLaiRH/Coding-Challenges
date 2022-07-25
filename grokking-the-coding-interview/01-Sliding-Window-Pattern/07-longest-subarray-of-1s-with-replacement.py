# Problem Statement
'''
Given an array containing 0s and 1s, if you are allowed to replace no more than 'k' 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.
'''

import unittest


def maxSubarrayOf1sWithReplacement(a, k):
    start, longest, onesCount = 0, 0, 0

    for end in range(len(a)):
        endNum = a[end]

        if endNum == 1:
            onesCount += 1

        while (end-start+1) - onesCount > k:
            if a[start] == 1:
                onesCount -= 1
            start += 1

        longest = max(longest, end-start+1)
    return longest


class Tests(unittest.TestCase):
    def test1(self):
        a = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
        self.assertEqual(maxSubarrayOf1sWithReplacement(a, 2), 6)

    def test2(self):
        a = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
        self.assertEqual(maxSubarrayOf1sWithReplacement(a, 3), 9)

    def test1V2(self):
        a = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
        self.assertEqual(maxSubarrayOf1sWithReplacement(a, 2), 6)

    def test2V2(self):
        a = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
        self.assertEqual(maxSubarrayOf1sWithReplacement(a, 3), 9)


# Note
'''
- Pretty much exactly the same as the book solution, but they did not use a endNum type variable which is fine just to remove a couple lines
'''

if __name__ == '__main__':
    unittest.main()
