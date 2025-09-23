class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            total = 0
            for c in range(COLS):
                total += matrix[r][c]
                above = self.prefix[r][c + 1]
                self.prefix[r + 1][c + 1] = total + above
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottom_right = self.prefix[row2][col2]
        above = self.prefix[row1 - 1][col2]
        left = self.prefix[row2][col1 - 1]
        above_left = self.prefix[row1 - 1][col1 - 1]
        return bottom_right - above - left + above_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)