class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def dfs(i, open_count):
            if open_count < 0:
                return False

            if i == len(s):
                return open_count == 0

            if (i, open_count) in memo:
                return memo[(i, open_count)]

            if s[i] == '(':
                memo[(i, open_count)] = dfs(i+1, open_count+1)
            elif s[i] == ')':
                memo[(i, open_count)] = dfs(i+1, open_count-1)
            else:
                memo[(i, open_count)] = (
                    dfs(i+1, open_count) or
                    dfs(i+1, open_count+1) or
                    dfs(i+1, open_count-1)
                )
            
            return memo[(i, open_count)]
            
        return dfs(0, 0)