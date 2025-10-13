class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for dislike in dislikes:
            adj_list[dislike[0]].append(dislike[1])
            adj_list[dislike[1]].append(dislike[0])
        
        def bfs(i):
            queue = deque([i])
            color[i] = 0

            while queue:
                node = queue.popleft()

                for neighbor in adj_list[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
            
            return True
        
        color = [-1] * (n+1)

        for i in range(1, n+1):
            if color[i] == -1:
                if not bfs(i):
                    return False
        
        return True
