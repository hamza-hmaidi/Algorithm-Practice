class MinStack:
    stack = []
    minimum  = float('inf')
    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.minimum = min(val,self.minimum)
        self.stack.append((val,self.minimum))    

    def pop(self) -> None:
        self.stack.pop()
        if(len(self.stack)==0):
            self.minimum=float('inf')
            return
        c= self.stack.pop()
        self.minimum = c[1]
        self.stack.append(c)
    def top(self) -> int:
        c = self.stack.pop()
        self.stack.append(c)
        return c[0]
    def getMin(self) -> int:
        c = self.stack.pop()
        self.stack.append(c)
        return c[1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()