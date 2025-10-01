class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(curr[j + 1], prev[j])
            prev, curr = curr, prev

        return prev[0]
        
        # dp = [[0 for j in range(len(text2) + 1)]
        #          for i in range(len(text1) + 1)]

        # for i in range(len(text1) - 1, -1, -1):
        #     for j in range(len(text2) - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # return dp[0][0]
        
        # memo = {}

        # def dfs(i, j, memo):
        #     if i == len(text1) or j == len(text2):  # checking if our pointers reach the end of text1 or text2
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if text1[i] == text2[j]:
        #         memo[(i, j)] = 1 + dfs(i + 1, j + 1, memo)
        #     else:
        #         memo[(i, j)] = max(dfs(i + 1, j, memo), dfs(i, j + 1, memo))

        #     return memo[(i, j)]

        # return dfs(0, 0, memo)