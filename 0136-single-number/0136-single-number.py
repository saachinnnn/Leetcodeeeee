from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Hashmap : dict = Counter(nums)

        for element,count in Hashmap.items():
            if count == 1:
                return element