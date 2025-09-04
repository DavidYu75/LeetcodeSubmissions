class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Build a set of all prefixes from arr1
        # find the prefix by repeatedly removing the last digit
        prefixes = set()
        for num in arr1:
            pre = num  # 123
            while pre > 0:
                prefixes.add(pre)
                pre //= 10  # remove the last digit -> keeps the leftmost prefix

        # for each number in arr2, we can remove the digits from the right until a prefix is found in the set
        # the first time we get a match with a prefix in our set, that would be by defaul the longest prefix
        # track global longest prefix

        longest_prefix = 0

        for num in arr2:
            pre = num

            length = 0
            digit_count = pre
            while digit_count > 0:
                length += 1
                digit_count //= 10
            
            while pre > 0:
                if pre in prefixes:
                    longest_prefix = max(longest_prefix, length)
                    break
                pre //= 10
                length -= 1
        
        return longest_prefix

        # time: O(D) where D is the total digits across all the numbers in arr1 and arr2
        # space: O(n) where n is the total digits across all numbers in arr1