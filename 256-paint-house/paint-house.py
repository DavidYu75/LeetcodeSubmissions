class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # red: 0, blue: 1, green: 2

        # space: O(4*n)
        # time: O(4*n)

        n = len(costs)
        memo = [[-1] * 4 for _ in range(n)]
        
        def dfs(i, prev_color):
            if i == n:
                return 0

            if memo[i][prev_color] != -1:
                return memo[i][prev_color]
            
            result = float('inf')
            for c in range(3):
                if c == prev_color:
                    continue
                result = min(result, costs[i][c] + dfs(i+1, c))
            
            memo[i][prev_color] = result

            return memo[i][prev_color]
        
        return dfs(0, -1)
