from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        Dictionary : dict = Counter(nums)
        for key in Dictionary:
            if Dictionary[key] == 1:
                return key
        return -1
