# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # [1, [2, 2], [[3], 2], 1]
        # 1*1 + 2*2 + 2*2 + 3*3 + 2*2 + 1*1 = 
        # 1 + 4 + 4 + 9 + 4 + 1 = 23

        # [[1, 1], 2, [1, 1]]
        #   2, 2 , 1,  2, 2

        # [[[1]]]

        # dfs that traverses through the nested list
        # we keep going deeper until we find the integer
        # once we find that integer, we will get the value then multiply it by its depth
        # dfs(nested_list, depth)
        # base case: if the nested_list is an integer, we know to stop get the current depth * the integer and add it to the result
        # dfs(new_nested_list, depth + 1)

        def dfs(nested_list, depth):
            result = 0

            for nested in nested_list:
                if nested.isInteger():
                    result += nested.getInteger() * depth
                else:
                    result += dfs(nested.getList(), depth + 1)
            
            return result
        
        return dfs(nestedList, 1)