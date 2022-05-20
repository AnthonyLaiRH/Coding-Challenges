# Problem
'''
Given a string, find the length of the longest substring which has no repeating characters.
'''
from curses import window
import unittest


def maxNoRepeatSubString(s):
    start, longest = 0, 0
    d = {}
    for end in range(len(s)):
        endLetter = s[end]
        if endLetter not in d:
            d[endLetter] = 0
        d[endLetter] += 1

        while d[endLetter] > 1:
            startLetter = s[start]
            d[startLetter] -= 1
            if d[startLetter] == 0:
                del d[startLetter]
            start += 1

        longest = max(longest, len(d))
    return longest


# Notes
'''
- The book solution shows that I can remove the complexity with the counting, if the letter is in the hash map its automatically not valid as a substring
- Look for these small things to remove complexity
- otherwise the solution is the same and remember remember to use hash maps and max() if possible
- the book uses 'end-start+1' to compare to the longest, this is what I should do as it is the more correct value (looking directly at the window we built)
'''

# Updated Code (this is the book solution directly)


def maxNoRepeatSubStringV2(s):
    start, longest = 0, 0
    d = {}
    for end in range(len(s)):
        endLetter = s[end]
        # if map already has endLetter, shrink window till only 1 instance of endLetter
        if endLetter in d:
          # endLetter is in the dict with value of its index in the string s
          # so we want to cut off everything from the first index of the endLetter in the window, which is stored at d[endLetter]
          # but we want to make sure that that postion isnt already behind us, hence the max comparison to start
            start = max(start, d[endLetter]+1)

        # place endLetter into the dict or update its value with the first index of endLetter in the window
        d[endLetter] = end

        longest = max(longest, end-start+1)
    return longest


class MyTest(unittest.TestCase):
    def test1(self):
        s = "aabccbb"
        self.assertEqual(maxNoRepeatSubString(s), 3)

    def test2(self):
        s = "abbbb"
        self.assertEqual(maxNoRepeatSubString(s), 2)

    def test3(self):
        s = "abccde"
        self.assertEqual(maxNoRepeatSubString(s), 3)

    def test1v2(self):
        s = "aabccbb"
        self.assertEqual(maxNoRepeatSubStringV2(s), 3)

    def test2v2(self):
        s = "abbbb"
        self.assertEqual(maxNoRepeatSubStringV2(s), 2)

    def test3v2(self):
        s = "abccde"
        self.assertEqual(maxNoRepeatSubStringV2(s), 3)


if __name__ == '__main__':
    unittest.main()
