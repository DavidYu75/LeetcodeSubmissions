class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        max_product, min_product = 1, 1

        for num in nums:
            temp = max_product * num
            max_product = max(max_product * num, min_product * num, num)
            min_product = min(temp, min_product * num, num)
            result = max(max_product, result)
        
        return result
