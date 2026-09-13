class MinStack:

    def __init__(self):
        self.elements = []
        self.length = 0

    def push(self, val: int) -> None:
        self.elements.append(val)
        self.length += 1

    def pop(self) -> None:
        self.elements.pop()

    def top(self) -> int:
        return self.elements[len(self.elements) -1]

    def getMin(self) -> int:
        min_val = self.elements[0]

        for el in self.elements:
            if el < min_val:
                min_val = el

        return min_val
