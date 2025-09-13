class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedsum = len(nums) * (len(nums) + 1) // 2
        actualsum = sum(nums)
        return expectedsum - actualsum