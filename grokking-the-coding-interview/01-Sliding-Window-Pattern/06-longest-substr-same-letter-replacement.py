# Problem Statement
'''
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
find the length of the longest substring having the same letters after replacement.
'''

import unittest


def longestSubStringOfSameAfterReplacement(s, k):
    start, maxSubstr, dominantCount = 0, 0, 0
    d = {}

    for end in range(len(s)):
        endChar = s[end]

        if endChar not in d:
            d[endChar] = 0
        d[endChar] += 1

        if d[endChar] > dominantCount:
            dominantCount = d[endChar]

        while (end-start+1)-dominantCount > k:
            startChar = s[start]
            d[startChar] -= 1
            if d[startChar] == 0:
                del d[startChar]

            start += 1
            dominantCount = max(d.values())

        maxSubstr = max(maxSubstr, end-start+1)

    return maxSubstr


# Notes
'''
- I was really close, but I knew my issue (checking all the values of d with max() each time there was a not valid window)
- The problem was I didnt recognize that I only need to shrink one spot at a time, as the size will only ever grow by one each time 
and I cant really skip over a chunk without increasing time complexity a bunch.
- Growing and shrinking by one each time allows us to check/update that dominantCount value every time
- Only on growing the window can the dominant value change realistically, this is because during shrinking if an occurrence of the dominant letter
is removed and the next add letter isnt a new dominant then the window is invalid anyways (thus the size doesnt change) and the max window doesnt change.

- eg. a a a b d c c c c  k=2
- See once the string is aaabd, dominantCount=3
 -> the window shrinks to aabd (max window is 5, so no change) 
 -> then the window grows to aabdc, dominantCount is still 3
 -> (5-1+1)-3=2, so no shrink, but max window is still 5 no change
 -> now aabdcc, dominantCount is still 3 
 -> (6-1+1)-3=3, so shrink to abdcc, max window still 5
 -> then abdccc, dominantCount=3 still, but now we're actually at c with 3 occurences
 -> then this shrinks to dbccc, but max window still hasnt moved
 -> bdcccc finally, now dominantCount=4 with the new c
 -> (8-3+1)-4=2 so its valid, and (8-3+1)=6 so we have a new max window too
'''


def longestSubStringOfSameAfterReplacementV2(s, k):
    start, maxSubstr, dominantCount = 0, 0, 0
    d = {}

    for end in range(len(s)):
        endChar = s[end]

        if endChar not in d:
            d[endChar] = 0
        d[endChar] += 1

        dominantCount = max(dominantCount, d[endChar])

        if (end-start+1)-dominantCount > k:
            startChar = s[start]
            d[startChar] -= 1
            start += 1

        maxSubstr = max(maxSubstr, end-start+1)

    return maxSubstr


class Tests(unittest.TestCase):
    def test1(self):
        s = "aabccbb"
        self.assertEqual(longestSubStringOfSameAfterReplacement(s, 2), 5)

    def test2(self):
        s = "abbcb"
        self.assertEqual(longestSubStringOfSameAfterReplacement(s, 1), 4)

    def test3(self):
        s = "abccde"
        self.assertEqual(longestSubStringOfSameAfterReplacement(s, 1), 3)

    def test1V2(self):
        s = "aabccbb"
        self.assertEqual(longestSubStringOfSameAfterReplacementV2(s, 2), 5)

    def test2V2(self):
        s = "abbcb"
        self.assertEqual(longestSubStringOfSameAfterReplacementV2(s, 1), 4)

    def test3V2(self):
        s = "abccde"
        self.assertEqual(longestSubStringOfSameAfterReplacementV2(s, 1), 3)

    def test4V2(self):
        s = "aaabbcccc"
        self.assertEqual(longestSubStringOfSameAfterReplacementV2(s, 2), 6)


if __name__ == '__main__':
    unittest.main()
