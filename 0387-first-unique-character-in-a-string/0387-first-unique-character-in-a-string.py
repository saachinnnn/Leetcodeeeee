class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Now I will solve this without the help of Counter.
        Hashmap : dict = {}
        for char in s:
            Hashmap[char] = Hashmap.get(char,0) + 1
        
        for character,count in Hashmap.items():
            if count == 1:
                return s.index(character)
        return -1