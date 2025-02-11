class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # first = 0
        # result = [0] * len(nums)

        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         result[second] = nums[i]
        #         second += 1
        
        # for i in range(len(nums)):
        #     nums[i] = result[i]

        slow = 0

        # 0, 1, 0, 3, 12
        # i = 0: nums[i] = 0   first = 0: nums[first] = 0
        # i = 1: nums[i] = 1    first = 0: nums[first] = 0  result: nums[0] = 1 nums[1] = 1 final: 1 0 0 3 12
        # i = 2: nums[i] = 0    first = 0: nums[first] = 1 
        # i = 3: nums[i] = 3    first = 1: nums[first] = 0  result: nums[2] = 3 nums[3] = 3 final: 1 3 0 0 12
        # i = 4: nums[i] = 12   first = 2: nums[first] = 0  final: 1 3 12 0 0 
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1
            
            
        