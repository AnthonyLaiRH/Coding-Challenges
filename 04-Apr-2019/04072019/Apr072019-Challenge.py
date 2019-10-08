

def main(self):
    list = [(1,3),(5,8),(4,10),(20,25)]
    print (reducer(self,list))

def reducer(self, list):
    newList = []
    prevHigh= 0
    for tuple in list:
        if tuple[0]>prevHigh:
            newList.append(tuple)
            prevHigh = tuple[1]
        elif tuple[0]<=prevHigh
            newList.remove(len(newList)-1)
            
        
    return newList