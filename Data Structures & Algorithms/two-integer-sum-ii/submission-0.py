class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}

        for i in range(0, len(numbers)):

            remaining = target - numbers[i]
            if remaining in map:
                return [map[remaining] + 1, i + 1]

            map[numbers[i]] = i