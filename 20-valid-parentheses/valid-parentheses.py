class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_chars = list(s)

        for char in s_chars:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif len(stack) == 0 or stack.pop() != char:
                return False
            
        return len(stack) == 0