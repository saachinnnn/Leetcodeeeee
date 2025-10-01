class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
       # Trying with a new array.
       Prefixsum : list = [0]*len(nums)

       Prefixsum[0] = nums[0]

       for i in range(1,len(Prefixsum)):
            Prefixsum[i] = nums[i] + Prefixsum[i - 1]
       return Prefixsum
       