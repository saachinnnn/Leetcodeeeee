class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans : list = []
        for idx in range(len(nums)):
            ans.append(nums[nums[idx]])
        return ans