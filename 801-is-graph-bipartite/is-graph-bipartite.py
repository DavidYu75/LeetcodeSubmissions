class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph)  # map node to even or odd: odd = 1, even = -1

        def bfs(i):
            if odd[i]:
                return True
            
            queue = deque([i])
            odd[i] = -1

            while queue:
                node = queue.popleft()

                for nei in graph[node]:
                    if odd[nei] == odd[node]:
                        return False
                    elif not odd[nei]:
                        queue.append(nei)
                        odd[nei] = -1 * odd[node]
                    
            return True
        
        for i in range(len(graph)):
            if not bfs(i):
                return False
        
        return True
        