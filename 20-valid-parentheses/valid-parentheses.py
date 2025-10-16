class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {']': '[', '}': '{', ')': '('}
        stack = []

        for c in s:
            if c in close_open:
                if stack and stack[-1] == close_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0