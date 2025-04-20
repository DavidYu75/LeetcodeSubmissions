class Solution:
    # 1,8,6,2,5,4,8,3,7
    # 1, 7  # width = 8 area = 8
    # 8, 7  # width = 7 area = 49
    # 8, 3
    def maxArea(self, height: List[int]) -> int:
        total_max = 0
        first, last = 0, len(height) - 1

        while first < last:
            curr_max = 0
            if height[first] > height[last]:
                curr_max = (last - first) * height[last]
                total_max = max(curr_max, total_max)
                last -= 1
            else:
                curr_max = (last - first) * height[first]
                total_max = max(curr_max, total_max)
                first += 1
        
        return total_max
            