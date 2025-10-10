class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        memo = [[-1] * 4 for _ in range(n)]

        def dfs(i, prev_color):
            if i == n:
                return 0
            
            if memo[i][prev_color + 1] != -1:
                return memo[i][prev_color + 1]
            
            result = float('inf')
            for c in range(3):
                if c == prev_color:
                    continue
                result = min(result, costs[i][c] + dfs(i+1, c))
            
            memo[i][prev_color + 1] = result

            return result
        
        return dfs(0, -1)