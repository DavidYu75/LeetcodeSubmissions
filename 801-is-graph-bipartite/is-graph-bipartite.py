class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        def bfs(i):
            if color[i]:
                return True
            
            queue = deque([i])
            color[i] = -1

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if color[neighbor] == color[node]:
                        return False
                    elif not color[neighbor]:
                        queue.append(neighbor)
                        color[neighbor] = -1 * color[node]
            
            return True
        
        for i in range(len(graph)):
            if not bfs(i):
                return False
        
        return True
        