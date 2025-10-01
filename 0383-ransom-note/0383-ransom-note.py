from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # The simplest solution would be to compared both of the dictionaries.
        return True if Counter(ransomNote) <= Counter(magazine) else False