class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        longest_seq = 0
        current_num = 0
        current_seq = 0

        for num in hashset:
            if num - 1 not in hashset:
                current_num = num
                current_seq = 1

                while current_num + 1 in hashset:
                    current_seq += 1
                    current_num += 1

                longest_seq = max(longest_seq, current_seq)

        return longest_seq
