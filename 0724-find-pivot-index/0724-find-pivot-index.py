class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # First we calculate the Prefixsum for this.
        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]


        # Now we run another for loop to get the pivot index.
        for i in range(len(nums)):
            if i == 0:
                if nums[0] == nums[-1]:
                    return 0
                else:
                    continue
            if nums[i - 1] == (nums[-1] - nums[i]):
                return i
        return -1