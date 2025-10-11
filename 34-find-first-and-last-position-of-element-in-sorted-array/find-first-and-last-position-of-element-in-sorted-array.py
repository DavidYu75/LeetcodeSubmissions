class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

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


        # for i, num in enumerate(nums):
        #     if num == target:
        #         if result[0] == -1:
        #             result[0] = result[1] = i
        #         else:
        #             result[1] = i
        
        # return result
