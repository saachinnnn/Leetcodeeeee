class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # First we do the operations...
        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx + 1]:
                nums[idx] *= 2
                nums[idx + 1] = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right],nums[left] = nums[left],nums[right]
                left += 1
        return nums
            
        