class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1

        while left < right:
            middle = (left + right) // 2

            if arr[middle] < x:
                left = middle + 1
            else:
                right = middle
        
        left, right = left - 1, left

        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        return arr[left+1:right]
