class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i, j, memo):
            if i == len(text1) or j == len(text2):  # checking if our pointers reach the end of text1 or text2
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1, memo)
            else:
                memo[(i, j)] = max(dfs(i + 1, j, memo), dfs(i, j + 1, memo))

            return memo[(i, j)]

        return dfs(0, 0, memo)