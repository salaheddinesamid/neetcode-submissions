class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            rest = target - nums[i]
            if rest not in map:
                map[nums[i]] = i
            else:
                return [map[rest], i]