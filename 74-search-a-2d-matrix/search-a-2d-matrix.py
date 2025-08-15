class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])    # rows = 3, cols = 4
        low, high = 0, rows * cols - 1  # high = 11

        while low <= high:
            mid = (low + high) // 2 # 11 // 2 = 5

            num = matrix[mid // cols][mid % cols]   # matrix[5 // 4][5 % 4] matrix[1][1]

            if num == target:
                return True
            if num < target:
                low = mid + 1
            if num > target:
                high = mid - 1

        return False
            