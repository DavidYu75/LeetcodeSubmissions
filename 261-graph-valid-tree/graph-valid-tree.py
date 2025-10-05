class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        
        adj_list = defaultdict(list)
        visited = set()

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        queue = deque([(0, -1)])
        visited.add(0)

        while queue:
            node, previous = queue.popleft()

            for neighbor in adj_list[node]:
                if neighbor == previous:
                    continue 

                if neighbor in visited:
                    return False
                
                queue.append((neighbor, node))
                visited.add(neighbor)
        
        return len(visited) == n
        