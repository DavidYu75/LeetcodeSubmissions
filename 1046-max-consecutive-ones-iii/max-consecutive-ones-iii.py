class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window
        # left and right pointer of our window
        # whenever we run into a 0 and we have flips remaining, use that flip and increase the right pointer
        # but whenever we run into a 0 and we don't have any flips remaining, increase left pointer
        # if we remove 0s from our window when we increase our left pointer, then we also want to gain those flips back
        # max_number that keeps track of our maximum length

        left = 0
        zeros_flipped = 0
        max_count  = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_flipped += 1
            
            while zeros_flipped > k:
                if nums[left] == 0:
                    zeros_flipped -= 1
                
                left += 1
            
            max_count = max(max_count, right - left + 1)
        
        return max_count
