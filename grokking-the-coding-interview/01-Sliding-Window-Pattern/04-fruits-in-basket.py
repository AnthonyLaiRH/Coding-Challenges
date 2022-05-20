# Problem Statement
'''
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can't skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.
'''
import unittest


def fruitsBasket(t):
    b = []
    start, longest = 0, 0
    for end in range(len(t)):
        b += t[end]
        fruits = len(set(b))
        if longest < len(b) and fruits <= 2:
            longest = len(b)

        while fruits > 2:
            # mistake here, its not b[start+1:] its just b[1:] (cutting off the first digit)
            # went back and fixed in #03 as well
            b = b[1:]
            fruits = len(set(b))
            start += 1

    return longest


class MyTest(unittest.TestCase):
    def test1(self):
        t1 = ["a", "b", "c", "a", "c"]
        self.assertEqual(fruitsBasket(t1), 3)

    def test2(self):
        t2 = ["a", "b", "c", "b", "b", "c"]
        self.assertEqual(fruitsBasket(t2), 5)


if __name__ == '__main__':
    unittest.main()

# Notes
'''
- Again array manipulation mistakes, pretty basic. a[1:] to remove the first element
- Same problem as 03 but with k=2, solution in the book is same as their solution to 03.
    - using a hash map to determine the unique fruits
    - space complexity for the book solution is constant, while with my answer space complexity is O(n) 
      due to the use of a list and set (set is constant space though)
- Using a hash map achieves the window and count the uniques at the same time, which saves on space
    - which could be key since time at O(n) is pretty much set and cant be really improved
'''

# Updated code (with hash map)


def fruitsBasketv2(t):
    start, longest = 0, 0
    d = {}

    for end in range(len(t)):
        endFruit = t[end]
        if endFruit not in d:
            # just to initialize value
            d[endFruit] = 0

        d[endFruit] += 1

        while len(d) > 2:
            startFruit = t[start]
            d[startFruit] -= 1
            if (d[startFruit] == 0):
                del d[startFruit]

            start += 1

        longest = max(max, end-start+1)

    return longest
