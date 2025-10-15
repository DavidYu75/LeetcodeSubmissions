class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        curr_count = 0

        for num in nums:
            if num == 1:
                curr_count += 1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 0
        
        return max(curr_count, max_count)

        # left = 0

        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         left = right + 1
            
        #     max_count = max(max_count, right - left + 1)
        
        # return max_count


        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[j] == 0:
        #             break
        #         max_count = max(max_count, j - i + 1)
        
        # return max_count
            