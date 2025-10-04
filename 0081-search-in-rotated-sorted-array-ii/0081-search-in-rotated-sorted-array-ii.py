class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Brute forcing this first.

        for idx in range(len(nums)):
            if nums[idx] == target:
                return True
        return False