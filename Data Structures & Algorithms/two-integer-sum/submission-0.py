class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for i in range(len(nums)):
            r = target - nums[i]

            if nums[i] not in map:
                map[r] = i
            else:
                return [map[nums[i]], i]