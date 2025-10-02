class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # There exists a set approach to this as well.
        
        ## Defining a set approach with sliding window algorithm.

        windowset : set = set()

        for idx in range(len(nums)):

            if idx > k:
                windowset.remove(nums[idx - k - 1])
            
            if nums[idx] in windowset:
                return True
            
            windowset.add(nums[idx])
        return False