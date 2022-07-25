# Problem Statement
'''
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

1. abc
2. acb
3. bac
4. bca
5. cab
6. cba

If a string has 'n' distinct characters it will have n! permutations.
'''

import unittest


def permutationsInString(s: str, p: str) -> bool:
    start = 0
    count = {}
    for c in p:
        if c not in count:
            count[c] = 0
        count[c] += 1

    for end in range(len(s)):
        endChar = s[end]
        if endChar in count:
            count[endChar] -= 1
            
        if end - start == len(p)-1:
            # breaking this all() statement down
                # all() simply returns True if all elements of the iterable parameter is True (False and 0 = False)
                # inside the brackets, the v == 0 is just translating the number value v into True or False in terms of being 0 or not
                # (this helps because 0=False typically, but this reverses things so we dont have to apply another negation later)
                # then for each v in count.values we evaluate if v==0 and add that boolean to a tuple
                # which then all() evaluates as a whole 
            # We want to know if all the values in count are 0, meaning the window is valid
            if all(v == 0 for v in count.values()):
                return True
            else:
                startChar = s[start]
                if startChar in count:
                    count[startChar] += 1
                start +=1

    return False


class Tests(unittest.TestCase):
    def test1(self):
        s = "oidbcaf"
        p = "abc"
        self.assertEquals(permutationsInString(s, p), True)

    def test2(self):
        s = "odicf"
        p = "dc"
        self.assertEquals(permutationsInString(s, p), False)

    def test3(self):
        s = "bcdxabcdy"
        p = "bcdyabcdx"
        self.assertEquals(permutationsInString(s, p), True)

    def test4(self):
        s = "aaacb"
        p = "abc"
        self.assertEquals(permutationsInString(s, p), True)


if __name__ == '__main__':
    unittest.main()
