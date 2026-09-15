class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in "*-+/":
                number = int(tokens[i])
                stack.append(number)

            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if tokens[i] == "+":
                    result = self.addition(num2, num1)

                elif tokens[i] == "*":
                    result = self.mult(num2, num1)

                elif tokens[i] == "-":
                    result = self.sub(num2, num1)

                elif tokens[i] == "/":
                    result = self.div(num2, num1)

                stack.append(result)

        return stack.pop()

    def addition(self, a, b):
        return a + b

    def mult(self, a, b):
        return a * b

    def sub(self, a, b):
        return a - b

    def div(self, a, b):
        return int(a / b)