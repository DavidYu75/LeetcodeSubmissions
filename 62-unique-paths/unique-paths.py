class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down memoization
        # cache = [[0] * n for i in range(m)]

        # def dfs(r, c, cache):
        #     if r >= m or c >= n:
        #         return 0
        #     if cache[r][c] > 0:
        #         return cache[r][c]
        #     if r == m - 1 and c == n - 1:
        #         return 1

        #     cache[r][c] = dfs(r + 1, c, cache) + dfs(r, c + 1, cache)

        #     return cache[r][c]
        
        # return dfs(0, 0, cache)

        # bottom up

        prev_row = [0] * n

        for r in range(m - 1, -1, -1):
            curr_row = [0] * n
            curr_row[n - 1] = 1
            
            for c in range(n - 2, -1, -1):
                curr_row[c] = curr_row[c + 1] + prev_row[c]
            
            prev_row = curr_row
        
        return prev_row[0]