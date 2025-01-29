class Solution(object):
    # greatest can be equal to or greater than max
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # brute force:
        # time: O(n^2)
        # space: O(n)
        # result = []
        
        # for i in range(len(candies)):
        #     totalCandies = candies[i] + extraCandies
        #     result.append(True)
        #     for j in range(len(candies)):
        #         if candies[j] > totalCandies:
        #             result.pop()
        #             result.append(False)
        
        # return result
        
        # time: O(n)
        # space: O(n)
        # maxCandies = 0
        result = []
        maxCandies = max(candies)

        # for candy in candies:
        #     if candy > maxCandies:
        #         maxCandies = candy
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)

        return result
        