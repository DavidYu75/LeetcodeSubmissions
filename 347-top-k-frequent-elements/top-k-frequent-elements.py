class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        min_heap = []

        for num in freq_map.keys():
            heapq.heappush(min_heap, (freq_map[num], num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []

        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result