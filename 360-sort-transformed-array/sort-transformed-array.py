class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def transform(x):
            return (a * x * x) + (b * x) + c

        left, right = 0, len(nums) - 1
        result = []

        if a < 0:
            while left <= right:
                left_transformed, right_transformed = transform(nums[left]), transform(nums[right])

                if left_transformed < right_transformed:
                    result.append(left_transformed)
                    left += 1
                else:
                    result.append(right_transformed)
                    right -= 1
        else:
            while left <= right:
                left_transformed, right_transformed = transform(nums[left]), transform(nums[right])

                if left_transformed > right_transformed:
                    result.append(left_transformed)
                    left += 1
                else:
                    result.append(right_transformed)
                    right -= 1
            
            result.reverse()
        
        return result

        
        # for i in range(len(nums)):
        #     nums[i] = transform(nums[i])
        
        # return sorted(nums)
