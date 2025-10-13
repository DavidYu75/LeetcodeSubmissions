class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0

        for c in s:
            if c == '(':
                left_min, left_max = left_min + 1, left_max + 1
            elif c == ')':
                left_min, left_max = left_min - 1, left_max - 1
            else:
                left_min, left_max = left_min - 1, left_max + 1
            
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        
        return left_min == 0
        
        # memo = {}

        # def dfs(i, open_count):
        #     if open_count < 0:
        #         return False

        #     if i == len(s):
        #         return open_count == 0

        #     if (i, open_count) in memo:
        #         return memo[(i, open_count)]

        #     if s[i] == '(':
        #         result = dfs(i+1, open_count+1)
        #     elif s[i] == ')':
        #         result = dfs(i+1, open_count-1)
        #     else:
        #         result = (
        #             dfs(i+1, open_count) or
        #             dfs(i+1, open_count+1) or
        #             dfs(i+1, open_count-1)
        #         )

        #     memo[(i, open_count)] = result
            
        #     return memo[(i, open_count)]
            
        # return dfs(0, 0)
