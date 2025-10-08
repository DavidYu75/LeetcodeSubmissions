import heapq

class MaxStack:
    
    def __init__(self):
        self.stack = []
        self.heap = []
        self.remove = set()
        self.id = 0

    def push(self, x: int) -> None:
        self.stack.append((x, self.id))
        heapq.heappush(self.heap, (-x, -self.id))

        self.id += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.remove:
            self.stack.pop()
        
        x, removed_id = self.stack.pop()
        self.remove.add(removed_id)
        return x

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.remove:
            self.stack.pop()
        
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.remove:
            heapq.heappop(self.heap)
        
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.remove:
            heapq.heappop(self.heap)
        
        x, removed_id = heapq.heappop(self.heap)
        self.remove.add(-removed_id)
        return -x


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()