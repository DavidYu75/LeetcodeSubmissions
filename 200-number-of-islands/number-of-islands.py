class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # treat this grid as a graph, with 4 neighbors (right, left, up, and down)
        # whenever we encounter a 1, we want to check if its neighbors are also 1
        # we want to see how big this islands is
        # we know to stop the bfs whenever we encounter a 0 (water) or we reach an out of bounds position
        # to avoid cycles in our bfs, we can set each visited node to 0, so we don't revisit any visited node

        # loop through the grid, whenever we encounter a 1, we will run bfs on that positon
        # the bfs will find all the connecting 1s from that position and also set those positions to 0
        # this will help reduce any recalculations and ensure that we don't recalculate any land that is associated with that island
        # islands += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr >= ROWS or nr < 0 or nc >= COLS or nc < 0 or grid[nr][nc] == "0":
                        continue
                    
                    grid[nr][nc] = "0"
                    queue.append((nr, nc))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands

        # time: O(m*n)
        # space: O(m*n)