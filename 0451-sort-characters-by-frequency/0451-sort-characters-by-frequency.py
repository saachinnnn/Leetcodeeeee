from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # Complete Brute Force.
        FrequencyMap : dict = Counter(s)
        ans_str : list = []
        
        # Sorting the dictionary.
        SortedDictionary : list = sorted(FrequencyMap.items(),key = lambda x : x[1], reverse = True)
        for element,value in SortedDictionary:
            ans_str.append(element*value)
        return "".join(ans_str)
        