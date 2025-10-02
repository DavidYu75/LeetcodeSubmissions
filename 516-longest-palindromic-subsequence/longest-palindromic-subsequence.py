class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # cache = {}

        # def dfs(i, j):
        #     if i < 0 or j >= len(s):
        #         return 0

        #     if (i, j) in cache:
        #         return cache[(i, j)]
            
        #     if s[i] == s[j]:
        #         length = 1 if i == j else 2
        #         cache[(i, j)] = length + dfs(i - 1, j + 1)
        #     else:
        #         cache[(i, j)] = max(dfs(i - 1, j), dfs(i, j + 1))
            
        #     return cache[(i, j)]

        # for i in range(len(s)):
        #     dfs(i, i)   # odd length palindromes
        #     dfs(i, i+1)     # even length palindromes

        # return max(cache.values())

        return self.longestCommonSubsequence(s, s[::-1])

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        N, M = len(s1), len(s2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(N):
            for j in range(M):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[N][M]