class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 2:
            return False
        windowsum = sum(nums[:2])
        hashset = set()
        hashset.add(windowsum)
        for right in range(2,len(nums)):
            windowsum -= nums[right - 2]
            windowsum += nums[right]
            if windowsum in hashset:
                return True
            hashset.add(windowsum)
        return False