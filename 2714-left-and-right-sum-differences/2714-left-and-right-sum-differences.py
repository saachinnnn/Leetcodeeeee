class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Brute force would be to compute two arrays where we get prefix and suffixsums.
        leftsum : list = [0]*len(nums)
        for idx in range(len(nums) - 1):
            leftsum[idx + 1]  = leftsum[idx] + nums[idx]
        rightsum : list = [0]*len(nums)
        for idx in range(len(nums) - 1,0,-1):
            rightsum[idx - 1] = rightsum[idx] + nums[idx]

        # Now that we have computed both arrays which is memory expensive but O(2N) ~ O(N)
        # Thus.
        return [abs(leftsum[idx] - rightsum[idx]) for idx in range(len(nums))]

