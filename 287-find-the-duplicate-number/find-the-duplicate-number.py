class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]   # nums[0] = 1 | nums[1] = 3
            fast = nums[nums[fast]] # nums[nums[0]] = nums[1] = 3 | nums[nums[3]]

            if slow == fast:
                break

        slow2 = 0

        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow
        
