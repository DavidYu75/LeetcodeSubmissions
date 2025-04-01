import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        # k_most = []

        # while len(k_most) < k:
        #     most_frequent = 0
        #     most_frequent_num = 0

        #     for num in hashmap:
        #         if hashmap[num] > most_frequent:
        #             most_frequent = hashmap[num]
        #             most_frequent_num = num

        #     k_most.append(most_frequent_num)
        #     del hashmap[most_frequent_num]

        heap = []

        for num, freq in hashmap.items():
            heapq.heappush(heap, [freq, num])

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
