class MinStack:

    def __init__(self):
        # use a python list to build stack
        self.stack = []
        self.minStack = [] # maintain the prefix mnimum element
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or self.minStack[-1] > val:
            # if len(self.stack) == 0 or self.minStack[-1] > val:// wrong, should check minStack
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if len(self.stack) == 0:
            raise IndexError("pop from an empty stack")
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            raise IndexError("empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) == 0:
            raise IndexError("empty stack")
        return self.minStack[-1]
