class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        if not stones:
            return 0

        # 1,1,2,4,7,8
        # x = 7, y = 8
        # 8 - 7 = 1
        # 1, 1, 1, 2, 4

        while len(stones) > 1:
            stones.sort()   # nlogn

            y = stones.pop()    # 1
            x = stones.pop()    # 1

            if x != y:
                new_stone = y - x
                stones.append(new_stone)    # 1
        
        if stones:
            return stones[0]
        else:
            return 0