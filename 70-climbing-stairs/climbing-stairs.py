class Solution:
    def climbStairs(self, n: int) -> int:
        # def dfs(i):
        #     if i >= n:
        #         return i == n
            
        #     return dfs(i + 1) + dfs(i + 2)
        
        # return dfs(0)

        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one