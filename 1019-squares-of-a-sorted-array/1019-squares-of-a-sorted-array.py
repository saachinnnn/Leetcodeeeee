class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # All we have to do is sort the array using abs by left and right pointer.
        l , r = 0 , len(nums) - 1
        ans : list = [0]*len(nums)
        idx = len(nums) - 1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                ans[idx] = (nums[r] * nums[r])
                idx -= 1
                r -= 1
            else:
                ans[idx] = (nums[l] * nums[l])
                idx -= 1
                l += 1
        return ans
            