class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            grid[r][c] = "0"
            queue = deque([(r, c)])

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr >= ROWS or nc >= COLS or nr < 0 or nc < 0 or grid[nr][nc] == "0":
                        continue
                    
                    grid[nr][nc] = "0"
                    queue.append((nr, nc))
                        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands
