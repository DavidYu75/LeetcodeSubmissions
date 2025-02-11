class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # second = 0

        # result = [0] * len(nums)

        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         result[second] = nums[i]
        #         second += 1
        
        # for i in range(len(nums)):
        #     nums[i] = result[i]

        # length = len(nums)

        # for i in range(length):
        #     print("i: ", nums[i])
        #     if nums[i] == 0:
        #         nums.append(nums.pop(i))
        #         i -= 2
        #     print(nums)
        
        first = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums.insert(first, nums.pop(i))
                first += 1
                i -= 1
            
            
        