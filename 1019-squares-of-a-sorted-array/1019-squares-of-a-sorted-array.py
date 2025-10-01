class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # All we have to do is sort the array using abs by left and right pointer.
        l , r = 0 , len(nums) - 1
        ans : list = []
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                ans.append(nums[r] * nums[r])
                r -= 1
            else:
                ans.append(nums[l] * nums[l])
                l += 1
        ans.reverse()
        return ans
            