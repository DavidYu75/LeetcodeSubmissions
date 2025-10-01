class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dfs
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        # r, c
        # r + 1, c
        # r, c + 1

        # dfs we want to take in our current row and col in our search (parameters)
        # we want to explore each path we can take if we either go down or go right
        # base cases:
        # current row is greater than the row dimension or current col is greater than the col direction
        # current row or current col is at 1 (obstacle)
        # current row and current col is at the bottom right corner, we found a valid path

        # cache = number of possible paths from that cell
        # cache = copy of our current grid but with all 0s, dynamically update each position in our grid with the possible paths from that position in our cache (this is to avoid duplicate calculations)
        # if our current r and c already in the cache, then we will just reference it instead of doing the same calculation
        cache = [[0] * COLS for i in range(ROWS)]
        
        def dfs(r, c, cache):
            if r >= ROWS or c >= COLS or obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            cache[r][c] = dfs(r + 1, c, cache) + dfs(r, c + 1, cache)

            return cache[r][c]

        # removed the choice of going down or right (2 choices)
        # going through every row and col in our grid
        # time : O(m * n)
        # space: O(m * n)
        return dfs(0, 0, cache)