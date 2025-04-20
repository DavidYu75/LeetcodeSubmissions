class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(['+', '-', '*', '/'])
        stack = []

        # 2, 1, +, 3, *
        # 2
        # 2, 1
        # num1 = 1
        # num2 = 2
        # 3
        # 3, 3
        # 9
        for token in tokens:
            if token in operations:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    stack.append(int(num2+ num1))
                elif token == '-':
                    stack.append(int(num2 - num1))
                elif token == '*':
                    stack.append(int(num2 * num1))
                else:
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(token))
        
        return stack[0]