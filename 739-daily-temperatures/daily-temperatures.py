class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                popped_index = stack.pop()
                result[popped_index] = (i - popped_index)
            stack.append(i)
        
        return result