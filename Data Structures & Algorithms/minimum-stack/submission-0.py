class MinStack:

    def __init__(self):
        self.main=[]
        self.minin=[]
        

    def push(self, val: int) -> None:
        self.main.append(val)
        if not self.minin:
            self.minin.append(val)
        else:
            self.minin.append(min(val, self.minin[-1]))

    def pop(self) -> None:
        self.main.pop()
        self.minin.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.minin[-1]
