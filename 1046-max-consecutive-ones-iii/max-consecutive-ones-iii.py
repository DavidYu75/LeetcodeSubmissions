class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # window that keeps track of 1s in the array
        # expand this window whenever we encounter a 1
        # whenever we encounter a 0 and we have flips available, flip this 0 to a 1
        # whenever we encounter a 0 and we don't have flips available, lets calculate window size
        # compare this window size with the current max_number 
        # shrink our window to our current index, and if we remove any 0s from our window, gain those flips back
        
        max_result = 0
        left = 0
        zeros_flipped = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_flipped += 1
            
            while zeros_flipped > k:
                if nums[left] == 0:
                    zeros_flipped -= 1
            
                left += 1
            
            max_result = max(max_result, right - left + 1)
        
        return max_result

        # time: O(n)
        # space: O(1)
