class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # tx in {x-1, x} tf in {y-1, y}
        # iterate through each coordinate for each black cell, we can increment a counter for each valid affected top left corner
        # count how many 2x2 blocks contain exactly 0-4 black cells
        # compare counts for 1 - 4 

        if m < 2 or n < 2:
            return [0,0,0,0,0]
        
        black_set = set((x,y) for x,y in coordinates)

        block_counts = defaultdict(int)

        for x, y in black_set:
            for tx in (x - 1, x):
                for ty in (y - 1, y):
                    if 0 <= tx < m - 1 and 0 <= ty < n - 1:
                        block_counts[(tx, ty)] += 1
        
        result = [0] * 5

        for cnt in block_counts.values():
            if 1 <= cnt <= 4:
                result[cnt] += 1
        
        total_blocks = (m - 1) * (n - 1)

        result[0] = total_blocks - sum(result[1:])

        return result