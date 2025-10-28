class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prefixarray : list = [0]*len(pref)
        prefixarray[0] = pref[0]
        for idx in range(1,len(pref)):
            prefixarray[idx] = pref[idx - 1]^pref[idx]
        return prefixarray