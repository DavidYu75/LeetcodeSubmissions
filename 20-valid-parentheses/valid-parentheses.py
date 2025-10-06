class Solution:
    def isValid(self, s: str) -> bool:
        opening_close = {'}': '{', ']': '[', ')': '('}
        stack = []

        for c in s:
            if c in opening_close:
                if stack and stack[-1] == opening_close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0