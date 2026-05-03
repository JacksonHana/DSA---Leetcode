#stack      -1  0   1   -2   
#minstack   -1  -1  -1  -2  

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])       # the top value in stack
        else: val = val 
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()


    def top(self) -> int:
        return self.stack[-1]                           # top value in stack

    def getMin(self) -> int:
        return self.minstack[-1]                        # top value in min stack


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()