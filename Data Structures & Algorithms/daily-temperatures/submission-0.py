class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)

        for slow in range(0, len(temperatures)):
            for fast in range(slow + 1, len(temperatures)):
                if temperatures[fast] > temperatures[slow]:
                    result[slow] = fast - slow
                    break

        return result
