class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       # For Maximum Subarray Type questions we can use Kadanes Algorithm.
       Result : int = nums[0]

       Maxending : int = nums[0]

       for i in range(1,len(nums)):
            Maxending = max(Maxending + nums[i],nums[i])
            Result = max(Maxending,Result)
       return Result