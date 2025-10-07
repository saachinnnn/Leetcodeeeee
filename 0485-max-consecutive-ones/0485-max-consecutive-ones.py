class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #I am going to try to solve this using sliding window approach.
        # It reduces this O(N2) to O(N).

        if len(nums) <= 0:
            return 0
        
        maxones : int = 0
        count : int = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                maxones = max(maxones,count)
                count = 0
            else:
                count += 1
        return max(maxones,count)