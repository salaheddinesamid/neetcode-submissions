class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i in range(0, len(nums)):
            r = target - nums[i]

            if r in map:
                return [map[r], i]
            
            map[nums[i]] = i