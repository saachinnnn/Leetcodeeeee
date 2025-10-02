from collections import Counter
import numpy as np
from itertools import chain
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans : list = []
        freq1 : dict = Counter(nums1)
        freq2 : dict =Counter(nums2)

        for ele,count in freq1.items():
            if ele in freq2:
                if freq1[ele] > freq2[ele]:
                    ans.append([ele]*freq2[ele])
                else:
                    ans.append([ele]*freq1[ele])
        return list(chain.from_iterable(ans))