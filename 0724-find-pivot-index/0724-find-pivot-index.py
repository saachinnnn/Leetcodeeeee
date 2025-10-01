class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Now doing the Totalling method.
        Total : int = sum(nums)
        LeftTotal : int = 0

        # Now looping once.
        for i in range(len(nums)):
            RightTotal : int = Total - LeftTotal - nums[i]

            if RightTotal == LeftTotal:
                return i
            LeftTotal += nums[i]
        return -1