class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 - red
        # 1 - white
        # 2 - blue

        counts = [0, 0, 0]

        for i in nums:
            counts[i] += 1
        
        b = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[b] = i
                b += 1
        
        