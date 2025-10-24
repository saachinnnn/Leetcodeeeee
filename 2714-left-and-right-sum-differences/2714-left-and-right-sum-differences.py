class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # One of the most clever solutions would be....
        leftsum : int = 0
        rightsum : int = sum(nums) # Precomputing the values.
        
        answer : list = []
        for idx in range(len(nums)):
            answer.append(abs(leftsum - (rightsum - nums[idx])))
            leftsum += nums[idx]
            rightsum -= nums[idx]
        return answer