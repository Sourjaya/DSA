class MinStack:
    
    def __init__(self):
        self.stack=[]
        self.maxStack=[]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.maxStack:
            val=max(val,self.maxStack[-1])
        self.maxStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.maxStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMax(self) -> int:
        return self.maxStack[-1]