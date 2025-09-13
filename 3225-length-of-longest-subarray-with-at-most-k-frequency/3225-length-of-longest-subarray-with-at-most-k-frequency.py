from collections import defaultdict 
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Optimal way.
        ## Edge cases...
        if k <= 0:
            return 0
        
        freq = defaultdict(int)
        l = 0
        maxlength = 0

        for r in range(len(nums)):
            freq[nums[r]] += 1

            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            
            maxlength = max(maxlength,r - l + 1)
        return maxlength