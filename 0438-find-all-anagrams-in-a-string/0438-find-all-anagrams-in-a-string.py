from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) <= 0 or len(p) <= 0:
            return []
        
        p_counter = Counter(p)
        windowcounter = Counter()
        result = []

        for i in range(len(s)):
            windowcounter[s[i]] += 1

            if i >= len(p):
                left_char = s[i - len(p)]
                windowcounter[left_char] -= 1
                if windowcounter[left_char] == 0:
                    del windowcounter[left_char]
            
            if windowcounter == p_counter:
                result.append(i- len(p) + 1)
        return result