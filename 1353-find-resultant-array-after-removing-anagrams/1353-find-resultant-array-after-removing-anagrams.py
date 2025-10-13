from collections import Counter
from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for word in words[1:]:
            if Counter(word) != Counter(result[-1]):
                result.append(word)
        words = result
        return words