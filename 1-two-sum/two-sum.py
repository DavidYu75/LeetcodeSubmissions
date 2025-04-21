class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = 2, 7, 11, 15
        # target = 9
        # output = 0, 1

        # nums = 3, 2, 4
        # target = 6
        # output = 1, 2

        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         if nums[j] == complement:
        #             return [i, j]

        hashmap = {}

        # 2: 0
        # 7: 1
        # 11: 2
        # 15: 3

        for i in range(len(nums)):
            hashmap.update({nums[i]: i})
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        
        return []