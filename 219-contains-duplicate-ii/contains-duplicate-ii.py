class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashmap = {}

        # for i in range(len(nums)):
        #     if nums[i] in hashmap and i - hashmap[nums[i]] <= k:
        #         return True
        #     hashmap[nums[i]] = i
        
        # return False

        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1

            if nums[right] in window:
                return True
            window.add(nums[right])

        return False
