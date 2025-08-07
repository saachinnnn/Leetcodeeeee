class MinStack:

    def __init__(self):
        self.stack : list = []
        self.minstack : list = []

    def push(self, val: int) -> None:
        if not self.minstack:
            self.minstack.append(val)
        elif self.minstack[-1] >= val:
            self.minstack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        element = self.stack.pop()
        if element == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()