# Notion Log Link:
# https://www.notion.so/anthonylairh/Container-with-Most-Water-11-Oct-8th-2019-f0383a097fe043e8bab0797c9d21f702

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        c = 0
        r = len(height)-1
        biggestProd = 0
        while (c != r):
            valC = height[c]
            valR = height[r]
            
            small = 0;
            
            if (valC > valR):
                small = valR
            else:
                small = valC
            
            prod = small*(r-c)
            
            if (prod > biggestProd):
                biggestProd = prod
                
            if (valC > valR):
                r-=1
            else:
                c+=1 
        
        return biggestProd