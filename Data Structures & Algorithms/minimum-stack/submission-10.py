class MinStack:

    def __init__(self):
        self.elements = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.elements.append(val)

        if not self.min_stack : 
            self.min_stack.append(val)
        else:
            self.min_stack.append(
                min(val, self.min_stack[-1])
            )

    def pop(self) -> None:
        self.elements.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.elements[len(self.elements) -1]

    def getMin(self) -> int:
        return self.min_stack[-1]
