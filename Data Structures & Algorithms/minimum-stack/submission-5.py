class MinStack:

    def __init__(self):
        self.elements = []
        self.minstack = []
        self.length = 0

    def push(self, val: int) -> None:

        self.elements.append(val)

        if not self.minstack:
            self.minstack.append(val)
        else:
            min_element = min(val, self.minstack[-1])
            self.minstack.append(min_element)
            

    def pop(self) -> None:
        self.elements.pop()
        self.minstack.pop()
        self.length -= 1

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.minstack[-1]