class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build an adjacency list and in degree counts
        # prereq -> list of courses dependent on it
        # ex: 0 -> [1]
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # initialize a queue where we first enter in the courses that have no prereqs
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        # kahn's algorithm
        while queue:
            node = queue.popleft()
            order.append(node)
            for next in graph[node]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    queue.append(next)
        
        return order if len(order) == numCourses else []

        # test cases
    

