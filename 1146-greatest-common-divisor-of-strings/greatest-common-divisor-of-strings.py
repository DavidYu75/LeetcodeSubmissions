class Solution(object):

    # ABCABC
    # ABC
    # ABCABC/ABC = 2
    # ABC/ABC = 1

    # ABABAB, ABAB
    # AB
    # ABABAB/AB = 3
    # ABAB = 2
    # len(ABABAB) = 6
    # len(ABAB) = 4
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # time: O(n)
        # space: O(n)
        factors = []
        for i in range(1, min(len(str1), len(str2)) + 1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                factors.append(i)

        divisor = ""

        for i in range(len(factors)):
            divisor = str1[:factors[len(factors) - i - 1]]
            repeated_count1 = len(str1) // len(divisor)
            repeated_count2 = len(str2) // len(divisor)

            if divisor * repeated_count1 == str1 and divisor * repeated_count2 == str2:
                break

            divisor = ""
        
        return divisor
        