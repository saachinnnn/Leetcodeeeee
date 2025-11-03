class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans : list = [0]*len(nums)
        for idx in range(len(nums)):
            ans[idx] = nums[nums[idx]]
        return ans