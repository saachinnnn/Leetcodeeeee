class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Brute force.
        ans : list = [0]*len(nums)
        for idx in range(len(nums)):
            count = 0
            for jdx in range(len(nums)):
                if idx != jdx and nums[idx] > nums[jdx]:
                    count += 1
            ans[idx] = count
        return ans
        