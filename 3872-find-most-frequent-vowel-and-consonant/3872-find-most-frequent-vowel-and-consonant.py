from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vmax : int = 0
        cmax : int = 0

        Hashmap : dict = Counter(s)

        for character in Hashmap:
            if character in ['a','e','i','o','u']:
                vmax = max(vmax,Hashmap[character])
            else:
                cmax = max(cmax,Hashmap[character])
        return vmax + cmax
