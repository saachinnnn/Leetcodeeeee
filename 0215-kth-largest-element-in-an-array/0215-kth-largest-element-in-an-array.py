class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # I will sort for now.
        nums.sort()
        return nums[-k]
            