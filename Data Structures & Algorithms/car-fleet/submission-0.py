class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse= True)

        stack = []

        for ps, speed in cars:
            arrival_time = (target - ps) / speed

            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)

        return len(stack)
