class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # So I am going to implement a hashmap that stores the elements and their indices.
        
        # Edge case.
        if len(nums) < 2:
            return False
        
        DuplicateChecker : dict = {}

        for idx in range(len(nums)): # We traverse through the array
            if nums[idx] in DuplicateChecker:
                if abs(idx - DuplicateChecker[nums[idx]]) <= k:
                    return True
                else:
                    DuplicateChecker[nums[idx]] = idx
            else:
                DuplicateChecker[nums[idx]] = idx
        return False