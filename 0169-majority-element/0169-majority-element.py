from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq : dict = Counter(nums)
        total : int = 0
        for element in freq:
            if freq[element] > len(nums)//2:
                return element
        return -1