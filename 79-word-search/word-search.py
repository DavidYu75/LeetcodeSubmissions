class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # word into a character array [A, B, C, C, E, D]
        # queue.popleft = O(1)
        # popping from array = O(n)
        # traverse the graph until we find the first character in the array
        # check the neighbors of that array and see if it equals to next element in the array
        # do this by having a loop that goes through every character in the character array
        # repeat that until there are no more characters in the array
        # else restart the search until we find the first character in the array

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or board[r][c] == '#':
                return False

            board[r][c] = '#'
            result = (dfs(r+1, c, i+1) or dfs(r, c+1, i+1) or dfs(r-1, c, i+1) or dfs(r, c-1, i+1))
            board[r][c] = word[i]

            return result
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False