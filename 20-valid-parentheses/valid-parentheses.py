class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {'}': '{', ']': '[', ')': '('}
        stack = []

        for char in s:
            if char in close_open:
                if stack and stack[-1] == close_open[char]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(char)
        
        return False if stack else True
