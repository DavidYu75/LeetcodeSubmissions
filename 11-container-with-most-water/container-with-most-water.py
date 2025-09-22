class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers: 1 set to the beginning of the array, the other set to the end of the array
        # for height: we want to take the min height of the two pointers
        # move pointer based on the smaller height of the two pointers

        left, right = 0, len(height) - 1
        max_vol = 0

        while left < right:
            container_width = right - left
            container_height = min(height[left], height[right])

            current_vol = container_width * container_height

            max_vol = max(max_vol, current_vol)

            if height[right] == container_height:
                right -= 1
            else:
                left += 1
        
        return max_vol