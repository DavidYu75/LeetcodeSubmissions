class Solution:
    # 1, 2, 3, 4
    # 24, 12, 4, 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []

        # for i in range(len(nums)):
        #     multiplication = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         multiplication *= nums[j]
        #     result.append(multiplication)
        
        # return result

        # left_product = [1] * len(nums)
        # right_product = [1] * len(nums)

        # left_product = 1, 1, 2, 6
        # right_product = 24, 12, 4, 1
        # result = 24, 12, 8, 6
        
        # left
        # -1, 1, 0, -3, 3
        # 1, -1, -1, 0, 0
        # left_product[0] = 1
        # for i in range(1, len(nums)):
        #     left_product[i] = left_product[i-1] * nums[i-1]

        # right_product[len(nums) - 1] = 1
        # 4, 3, 2, 1
        # 1, 4, 12, 24
        # 1, 2, 3, 4
        # 1, 1, 1, 1
        # 24, 12, 4, 1
        # for i in range(len(nums) - 2, -1, -1):
        #     right_product[i] = right_product[i+1] * nums[i+1]

        # result = []
        # for i in range(len(left_product)):
        #     result.append(left_product[i] * right_product[i])

        # return result

        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
