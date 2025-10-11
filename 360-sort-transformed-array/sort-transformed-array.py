class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def transform(num):
            return (num * num * a) + (b * num) + c
        
        left, right = 0, len(nums) - 1
        answer = []

        if a < 0:
            while left <= right:
                left_transformed, right_transformed = transform(nums[left]), transform(nums[right])

                if left_transformed < right_transformed:
                    answer.append(left_transformed)
                    left += 1
                else:
                    answer.append(right_transformed)
                    right -= 1
        else:
            while left <= right:
                left_transformed, right_transformed = transform(nums[left]), transform(nums[right])

                if left_transformed > right_transformed:
                    answer.append(left_transformed)
                    left += 1
                else:
                    answer.append(right_transformed)
                    right -= 1
            answer.reverse()
        
        return answer
        
        # for i in range(len(nums)):
        #     nums[i] = apply_function(nums[i])

        # print(nums)
        
        # return sorted(nums)