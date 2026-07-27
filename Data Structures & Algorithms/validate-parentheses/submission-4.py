class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for b in s:

            # Opening bracket
            if b in '({[':
                stack.append(b)

            # Closing bracket
            else:
                if not stack:
                    return False

                opening = stack.pop()

                if opening != pairs[b]:
                    return False

        return len(stack) == 0
