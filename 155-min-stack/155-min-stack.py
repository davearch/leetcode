class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            _, prev_min = self.stack[-1] # tuple
        else:
            prev_min = float('inf')
        new_min = min(prev_min, val)
        self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        last_val, _ = self.stack[-1]
        return last_val

    def getMin(self) -> int:
        _, last_min = self.stack[-1]
        return last_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()