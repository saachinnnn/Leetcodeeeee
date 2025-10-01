from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # The Pythonic approach.
        freq = Counter(s)
        sortedfreq = sorted(freq.items(),key = lambda x : x[1],reverse = True)
        return "".join([element * count for element,count in sortedfreq])
        