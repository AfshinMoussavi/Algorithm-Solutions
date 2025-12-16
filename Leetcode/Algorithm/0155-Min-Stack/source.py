# Name: 155. Min Stack
# URL:  https://leetcode.com/problems/min-stack/description/



class MinStack:

    def __init__(self):
        self.items = []
        self.tracker = []
        
    def push(self, val: int) -> None:
        self.items.append(val)
        
        if len(self.tracker) == 0:
            self.tracker.append(val)
        else:
            self.tracker.append(min(self.tracker[-1], val))

    def pop(self) -> None:
        self.items.pop()
        self.tracker.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.tracker[-1]



