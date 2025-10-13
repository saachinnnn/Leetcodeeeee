class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # Brute Forcing this.
        ans : list = [words[0]]
        for idx in range(1,len(words)):
            if sorted(words[idx]) == sorted(words[idx - 1]):
                continue
            ans.append(words[idx])
        words = ans.copy()
        return words