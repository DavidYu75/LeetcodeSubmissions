class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numbers = {}

        # for i in range(len(nums)):
        #     numbers[nums[i]] = i

        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in numbers and numbers[complement] != i:
        #         return [i, numbers[complement]]
        
        # return []

        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            else:
                hashmap[nums[i]] = i
        
        return []