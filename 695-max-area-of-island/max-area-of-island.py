class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        max_area = 0

        def bfs(r, c):
            current_area = 1
            queue = deque()
            grid[r][c] = 0
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0):
                        continue
                    
                    queue.append((nr, nc))
                    current_area += 1
                    grid[nr][nc] = 0
            
            return current_area
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area