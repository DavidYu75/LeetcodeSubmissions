class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if we want the unique elements to appear at most twice, first two will always be unique
        if len(nums) <= 2:
            return len(nums)

        left = 2

        for right in range(2, len(nums)):
            if nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1
        
        return left