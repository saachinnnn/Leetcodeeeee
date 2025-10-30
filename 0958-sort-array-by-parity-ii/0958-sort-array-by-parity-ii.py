class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # Solving it inplace would be.
        if not nums:
            return []
        left = 0
        right = 1
        while left < len(nums) and right < len(nums):
            while left < len(nums) and nums[left] % 2 == 0:
                left += 2
            while right < len(nums) and nums[right] % 2 != 0:
                right += 2
            if left < len(nums) and right < len(nums):
                nums[left],nums[right] = nums[right],nums[left]
        return nums