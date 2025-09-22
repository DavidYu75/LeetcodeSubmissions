class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # the first element in the array will always be unique
        # keep two pointers: one for placement and one for scanning

        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        
        return left
            