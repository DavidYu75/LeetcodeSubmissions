class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # [1, 3], [-2, 2]
        # distance 1 = sqrt((1-0)^2 + (3-0)^2)
        # 1^2 + 3^2 = 10
        # distance 1 = sqrt(10)
        # distance 2 = sqrt((-2-0)^2 + (2-0)^2)
        # (-2)^2 + 2^2 = 8
        # distance 2 = sqrt(8)
        # sqrt(8) < sqrt(10)

        heap = []

        for point in points:
            x, y = point
            distance = x*x + y*y
            heapq.heappush(heap, (distance, point))
        
        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result