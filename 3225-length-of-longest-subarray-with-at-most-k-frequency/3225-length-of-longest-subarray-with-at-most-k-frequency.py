class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Edge Cases.
        if k == 0 or k < 0:
            return None 
        elif len(nums) == 0:
            return None 
        
        Hashmap : dict = {}
        Hashmap[nums[0]] = 1

        maxlength = 1
        l = 0
        for r in range(1,len(nums)):
            if nums[r] not in Hashmap:
                Hashmap[nums[r]] = 1
                maxlength = max(maxlength,r - l + 1)
            elif Hashmap[nums[r]] < k:
                Hashmap[nums[r]] += 1
                maxlength = max(maxlength,r - l + 1)
            else:
                while Hashmap[nums[r]] >= k:
                    Hashmap[nums[l]] -= 1
                    l += 1
                Hashmap[nums[r]] += 1
                maxlength = max(maxlength,r - l + 1)
        return maxlength
        
