class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for i in range(m)]

        def dfs(r, c, cache):
            if r >= m or c >= n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m - 1 and c == n - 1:
                return 1

            cache[r][c] = dfs(r + 1, c, cache) + dfs(r, c + 1, cache)

            return cache[r][c]
        
        return dfs(0, 0, cache)