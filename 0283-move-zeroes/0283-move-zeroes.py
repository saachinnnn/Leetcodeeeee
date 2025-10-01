class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L , R = 0 , 1
        while R < len(nums):
            if nums[R] != 0 and nums[L] == 0:
                nums[R],nums[L] = nums[L],nums[R]
                L += 1
                R += 1
            elif nums[L] != 0:
                L += 1
                if L == R:
                    R += 1
            else:
                R += 1
            