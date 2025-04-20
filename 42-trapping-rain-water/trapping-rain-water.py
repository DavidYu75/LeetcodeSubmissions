class Solution:
    def trap(self, height: List[int]) -> int:
        first, last = 0, len(height) - 1
        water_trapped = 0
        left_max = 0
        right_max = 0

        while first < last:
            if height[first] < height[last]:
                if height[first] > left_max:
                    left_max = height[first]
                else:
                    water_trapped += left_max - height[first]
                first += 1
            else:
                if height[last] > right_max:
                    right_max = height[last]
                else:
                    water_trapped += right_max - height[last]
                last -= 1
        
        return water_trapped