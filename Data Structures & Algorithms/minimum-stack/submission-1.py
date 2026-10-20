class MinStack:

    def __init__(self):
        # use a python list to build stack
        self.stack = []
        self.minStack = [] # maintain the prefix mnimum element, consider each nod ein stack has a corresponding minimum value

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
