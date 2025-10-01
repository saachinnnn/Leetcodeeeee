class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Apparently the simpler version.
        ## Even more simpler version....

        leftPtr : int = 0

        for rightptr in range(len(nums)):
            if nums[rightptr] != 0:
                nums[leftPtr] , nums[rightptr] = nums[rightptr] , nums[leftPtr]
                leftPtr += 1
        
            