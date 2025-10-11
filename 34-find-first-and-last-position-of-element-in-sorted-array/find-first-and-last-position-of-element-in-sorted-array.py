class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Input: nums = [5,7,7,8,8,10], target = 8
        # Output: [3,4]

        # nums = 5, 7, 7, 8, 8, 8,
        # output = [3, 5]

        # result array = [-1. -1]
        # loop through the num in nums
        # once we find the first occurence of our target, we can update result[0] = index
        # continue to loop through the numbers array until we find the last occurence
        # time complexity: O(n)
        # space: O(1)
        # result = [-1, -1]

        # for i, num in enumerate(nums):
        #     if num == target:
        #         if result[0] == -1:
        #             result[0] = result[1] = i
        #         else:
        #             result[1] = i
        
        # return result

        # binary search
        # middle of the array is less than the target: search the right half of the array
        # middle of the array is greater than the target: search the left half of the array
        # middle of the array is equal to the target: we want to make sure we have the left most and the right most
        # if we want the left most, we can continue to move our right pointer and shift it down
        # if we want the right most, we can continue to move our left pointer and shift it up
        # O(logn), space: O(1)
        result = [-1, -1]
        

        # left_bias: True then find left most, False then find the right most
        def binary_search(nums, target, left_bias):
            left, right = 0, len(nums) - 1
            i = -1

            while left <= right:
                middle = (left + right) // 2

                if nums[middle] < target:
                    left = middle + 1
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    i = middle
                    if left_bias:
                        right = middle - 1
                    else:
                        left = middle + 1
                
            return i
        
        result[0] = binary_search(nums, target, True)
        result[1] = binary_search(nums, target, False)

        return result
