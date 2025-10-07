class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # I will brute force this and end it right it here.
        ## Nah sike i am going to use a dictionary.

        ans : int = 0
        for right in range(len(nums)):
            if nums[right] in nums[right + 1:]:
                ans += nums[right + 1:].count(nums[right])
        return ans