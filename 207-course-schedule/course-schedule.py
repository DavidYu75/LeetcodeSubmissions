class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_prereq = { c:[] for c in range(numCourses)}

        for course, prereq in prerequisites:
            course_prereq[course].append(prereq)

        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)

            for pre in course_prereq[course]:
                if dfs(pre) == False:
                    return False
                
            cycle.remove(course)
            visited.add(course)
        
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        
        return True
