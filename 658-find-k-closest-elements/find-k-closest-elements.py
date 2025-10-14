class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if our target exists in the array, we want to find the index of our target
        # if our target doesn't exist, we want to get the index of the closest number in our array
        # we have two pointers that each point to each neighbor of our target.
        # 
        # to find our target: O(logn)
        # to find all the k integers closest to our target: O(k)
        # O(logn + k)
        # O(1)

        left, right = 0, len(arr) - 1

        while left < right:
            middle = (left + right) // 2

            if arr[middle] < x:
                left = middle + 1
            else:
                right = middle
        
        
        # arr[left] = number that is closest to the x
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
            