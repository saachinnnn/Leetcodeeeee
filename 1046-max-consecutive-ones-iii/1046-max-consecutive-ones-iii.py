class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # The simplest solution i found using maths.
        low : int = 0
        for high in range(len(nums)):
            if nums[high] == 0:
                k -= 1
            if k < 0:
                if nums[low] == 0:
                    k += 1
                low += 1
        return high - low + 1