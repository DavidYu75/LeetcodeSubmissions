class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        water_trapped = 0
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max > right_max:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
            else:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]

        return water_trapped
