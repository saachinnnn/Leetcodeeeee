class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Apparently the simpler version.
        insert_position : int = 0

        for num in nums:
            if num != 0:
                nums[insert_position] = num
                insert_position += 1
        for i in range(insert_position,len(nums)):
            nums[i] = 0
            