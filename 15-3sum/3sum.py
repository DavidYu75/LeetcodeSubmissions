class Solution:
    # -1, 0, 1, 2, -1, -4
    # -1    complement = 0 - -1 = 1
    # {
    #     -1: 0
    #     0 : 1
    #     1 : 2
    #     2: 3
    #     -1: 4
    #     -4: 5
    # }

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            first = i + 1
            last = len(nums) - 1

            while first < last:
                current_sum = nums[i] + nums[first] + nums[last]                    
                if current_sum < 0:
                    first += 1
                elif current_sum > 0:
                    last -= 1
                else:
                    results.append([nums[i], nums[first], nums[last]])
                    first += 1
                    while nums[first] == nums[first - 1] and first < last:
                        first += 1

        return results
