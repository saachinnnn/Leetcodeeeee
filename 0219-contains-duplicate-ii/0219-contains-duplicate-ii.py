class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # A bit better code would be.
        DuplicateChecker : dict = {}
        for idx , num in enumerate(nums):
            if num in DuplicateChecker and abs(idx - DuplicateChecker[num]) <= k:
                return True
            DuplicateChecker[num] = idx
        return False