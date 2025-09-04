class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # build an adjacency list where each number map to its adjacent neighbors
        neighbors = defaultdict(list)

        for u, v in adjacentPairs:
            neighbors[u].append(v)
            neighbors[v].append(u)

        # the two ends of an array should have a degree of 1
        start = None

        for val, adj in neighbors.items():
            if len(adj) == 1:
                start = val
                break
        # start at an endpoint (degree of 1) to begin reconstructing our array
        # walk the path of the adjacency list and at each step we choose the neighbor that is not the previous
        n = len(neighbors)
        result = [0] * n
        result[0] = start

        if n == 1:
            return result
        
        result[1] = neighbors[start][0]

        for i in range(2, n):
            prev = result[i - 2]
            curr = result[i - 1]
            a, *rest = neighbors[curr]

            if rest:
                b = rest[0]
                result[i] = a if a != prev else b
            else:
                result[i] = a
        
        return result

        # time: build an adjacency list from n amount of pairs, single pass through the array of n pairs
        # O(n)
        # space: build an ajacency list - stores all n elements. O(n)