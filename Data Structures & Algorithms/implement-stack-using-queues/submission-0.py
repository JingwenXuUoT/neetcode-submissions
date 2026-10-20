class MyStack:

    def __init__(self):
        self.q = deque()# double ended queue

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # pop from the queue, add to the tail, until the last element of queue, pop->O(n)
        for i in range(len(self.q)-1):
            # except the last value
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()