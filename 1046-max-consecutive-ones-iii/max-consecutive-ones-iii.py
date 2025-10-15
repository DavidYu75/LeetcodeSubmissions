class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_length = left = zero_count = 0

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

        # for i in range(n):
        #     zeros = 0
        #     for j in range(i, n):
        #         if nums[j] == 0:
        #             zeros += 1
        #         if zeros <= k:
        #             max_length = max(max_length, j - i + 1)
        #         else:
        #             i = j
        #             break
        
        # return max_length
