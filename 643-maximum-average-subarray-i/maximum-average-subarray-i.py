class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_total = sum(nums[:k])
        max_avg = curr_total / k

        for i in range(k, len(nums)):
            curr_total += nums[i] - nums[i - k]
            curr_avg = curr_total / k

            if curr_avg > max_avg:
                max_avg = curr_avg

        return max_avg
        