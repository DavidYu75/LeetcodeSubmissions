class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        first = 1
        last = max(piles)
        # 1 - 11 bananas per hours  that is our search range

        result = -1
        while first <= last:
            mid = (first + last) // 2   # 12 // 2 = 6

            hours_taken = 0
            for bananas in piles:
                hours_taken += math.ceil(float(bananas) / mid)
            
            if hours_taken > h:
                first = mid + 1
            else:
                result = mid
                last = mid - 1

        return result
        
