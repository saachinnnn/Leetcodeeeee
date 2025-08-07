from collections import deque
class MyQueue:

    def __init__(self):
        self.queue : list = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if len(self.queue) == 0:
            return None
        return self.queue.popleft()

    def peek(self) -> int:
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()