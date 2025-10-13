# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        self.idx = 0
        self.dfs(nestedList)
    
    def next(self) -> int:
        value = self.arr[self.idx]
        self.idx += 1

        return value
    
    def hasNext(self) -> bool:   
        if self.idx < len(self.arr):
            return True    
        else:
            return False 

    def dfs(self, nested_list):
        for nested in nested_list:
            if nested.isInteger():
                self.arr.append(nested.getInteger())
            
            self.dfs(nested.getList())

            

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())