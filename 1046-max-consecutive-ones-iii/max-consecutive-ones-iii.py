class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count = 0
        left = 0
        zeros_flipped = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_flipped += 1
            
            while zeros_flipped > k:
                if nums[left] == 0:
                    zeros_flipped -= 1
                
                left += 1
            
            max_count = max(max_count, right - left + 1)
        
        return max_count
