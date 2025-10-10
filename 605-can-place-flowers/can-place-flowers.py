class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        grid = [0] + flowerbed + [0]

        for i in range(1, len(grid) - 1):
            if grid[i - 1] == 0 and grid[i] == 0 and grid[i + 1] == 0:
                grid[i] = 1
                n -= 1
            
        return n <= 0
