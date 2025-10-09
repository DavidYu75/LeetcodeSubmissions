class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)


        # def bfs(r, c):
        #     queue = deque([(r, c)])
        #     grid[r][c] = "0"

        #     while queue:
        #         r, c = queue.popleft()

        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc

        #             if nr >= ROWS or nc >= COLS or nr < 0 or nc < 0 or grid[nr][nc] == "0":
        #                 continue
                    
        #             queue.append((nr, nc))
        #             grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
