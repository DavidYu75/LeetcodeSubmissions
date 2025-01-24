class Solution(object):
    # word1 = abc
    # word2 = pqr
    # word2 = rqp
    # apbqcr

    # word1 = ab
    # word2 = pqrs
    # word2 = srqp
    # ab srqp

    # apbqsr
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        # time: O(n)
        # space: O(1)
        result = ""

        point1 = 0
        point2 = 0

        for i in range(len(word1) + len(word2)):
            if point1 < len(word1):
                result += word1[point1:point1 + 1]
                point1 += 1
            if point2 < len(word2):
                result += word2[point2:point2+1]
                point2 += 1

        return result
            

        