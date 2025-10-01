class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       # For Maximum Subarray Type questions we can use Kadanes Algorithm.
       Result : int = nums[0]

       total : int = 0
       
       for num in nums:
            if total < 0:
                total = 0
            
            total += num
            Result = max(Result,total)
       return Result