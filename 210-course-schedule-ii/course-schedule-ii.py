class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_prereq = { course:[] for course in range(numCourses) }

        for course, prereq in prerequisites:
            course_prereq[course].append(prereq)

        visited, cycle = set(), set()
        output = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)

            for pre in course_prereq[course]:
                if dfs(pre) == False:
                    return False
            
            output.append(course)
            cycle.remove(course)
            visited.add(course)

            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return output