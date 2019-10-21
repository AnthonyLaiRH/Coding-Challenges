import re
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        prefixR = re.compile(prefix)
        s = 0
				
				# The idea of this one liner is for every key, value pair in map, add its value to this
				# array if it satisfies the condition following the if.
				# Then the sum() function just sums all the vlaues in the array
        s = sum([value for key, value in self.map.items() if (bool(prefixR.match(key)))])
        #### Expanded Version of the above one liner
        #for key, value in self.map.items():
        #    if bool(prefixR.match(key)):
        #        s += value
        return s

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)