class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_left = len(students)
        count = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
                students_left -= 1
            else:
                break
        
        return students_left
            