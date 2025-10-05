class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj_list = {i:[] for i in range(n)}
        visited = set()

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        queue = deque([(0, -1)])
        visited.add(0)

        while queue:
            node, prev = queue.popleft()

            for neighbor in adj_list[node]:
                if neighbor == prev:
                    continue
                
                if neighbor in visited:
                    return False

                queue.append((neighbor, node))
                visited.add(neighbor)
        
        return len(visited) == n
            

        
        # def dfs(i, prev):
        #     if i in visited:
        #         return False

        #     visited.add(i)
            
        #     for j in adj_list[i]:
        #         if j == prev:
        #             continue
                
        #         if not dfs(j, i):
        #             return False
                
        #     return True
        
        # return dfs(0, -1) and len(visited) == n
