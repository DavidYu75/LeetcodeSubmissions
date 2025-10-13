class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        
        partition = left

        def binary_search(left, right):
            while left <= right:
                middle = (left + right) // 2

                if nums[middle] < target:
                    left = middle + 1
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    return middle
        
            return -1
        
        result = binary_search(0, partition)
        if result != -1:
            return result
        
        return binary_search(partition, len(nums) - 1)
