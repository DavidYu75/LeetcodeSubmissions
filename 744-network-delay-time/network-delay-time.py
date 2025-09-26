class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create adj list
        adj_list = {}

        for i in range(1, n + 1):
            adj_list[i] = []

        for start, target, weight in times:
            adj_list[start].append([target, weight])

        # adj_list where each node key will store the target node and the weight of getting there

        shortest = {}   # hashmap that has node keys that store the shortest path from source to node
        min_heap = [[0, k]]

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj_list[n1]:     # checks the neighbors and calculates the shortest path to the neighbors
                if n2 not in shortest:
                    heapq.heappush(min_heap, [w1 + w2, n2])
        
        # since everything in the hashmap already contains the shortest path from source to every node
        # in order for all nodes to receive the signal, we take the maximum

        max_node = max(shortest.values())

        return max_node if len(shortest) == n else -1