class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val < self.minstack[-1][0]:
            self.minstack.append([val, 1])
        elif val == self.minstack[-1][0]:
            self.minstack[-1][1] += 1

    def pop(self) -> None:
        if self.minstack[-1][0] == self.stack[-1]:
            self.minstack[-1][1] -= 1

        if self.minstack[-1][1] == 0:
            self.minstack.pop()
        
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()