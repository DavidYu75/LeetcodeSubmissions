class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose the matrix
        # reverse each row
        rows = len(matrix)

        for i in range(rows):
            for j in range(i + 1, rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(rows):
            left = 0
            right = rows - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
        