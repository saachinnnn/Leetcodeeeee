class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Basically we calculate the prefix sum for the given array.
        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]
        return nums