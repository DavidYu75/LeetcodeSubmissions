class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        queue = deque()
        fresh_oranges = 0
        levels = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        while fresh_oranges > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh_oranges -= 1
            levels += 1
            
        return levels if fresh_oranges == 0 else -1
