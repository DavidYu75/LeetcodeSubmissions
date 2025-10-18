class Solution:
    def isValid(self, s: str) -> bool:
        # ()
        # ()[]{}
        # ([])
        # ([)]

        # ([)]

        # stack will be empty at the end if we have a valid string
        # hashmap, where we have each closing as a key, each value of that key maps to the opening counterpart
        # O(1)
        # O(n)

        close_open = {')': '(', ']': '[', '}': '{'}
        stack = []

        # )))
        # )

        for c in s:
            if c in close_open:
                if stack and stack[-1] == close_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0

        # time: O(n)
        # space: O(n)
