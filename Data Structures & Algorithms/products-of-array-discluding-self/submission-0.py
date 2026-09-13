class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        # calculate the products from left:
        prefix = 1 # initiate a prefix:
        for i in range(0, len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # calculate the products from the right
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result