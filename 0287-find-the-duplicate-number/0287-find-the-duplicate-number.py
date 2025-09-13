from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        Hashmap : dict = Counter(nums)
        for key in Hashmap:
            if Hashmap[key] > 1:
                return key