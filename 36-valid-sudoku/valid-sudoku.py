class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in board:
            hashrow = set()
            for num in row:
                if num == ".":
                    continue
                if num in hashrow:
                    return False
                hashrow.add(num)

        # columns
        for col in range(9):
            hashcol = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in hashcol:
                    return False
                hashcol.add(board[i][col])

        for square in range(9):
            hashsquare = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in hashsquare:
                        return False
                    hashsquare.add(board[row][col])
        
        return True