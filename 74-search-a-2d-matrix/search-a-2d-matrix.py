class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        
        rows, cols = len(matrix), len(matrix[0])

        start = 0
        end = rows * cols - 1  #11

        while start <= end:
            mid = (start + end) // 2    # (11 + 0) // 2 = 5

            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False


