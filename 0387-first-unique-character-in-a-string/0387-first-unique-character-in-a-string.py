from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
       Hashmaps : dict = Counter(s)
       for char in s:
            if Hashmaps[char] == 1:
                return s.index(char)
       return -1