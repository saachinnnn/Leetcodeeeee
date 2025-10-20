class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        if len(nums) <= 2:
            return max(nums)
        
        for iteration in range(2):
            value = max(nums)
            index = nums.index(value)
            # Now.
            nums[index] = -10000000000000000
        return max(nums)