class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # I will brute force this and end it right it here.
        ## Nah sike i am going to use a dictionary
        return sum(nums[right + 1:].count(nums[right]) if nums[right] in nums[right + 1:] else 0 for right in range(len(nums)))

        # Damnnnn the above solution is cool af.