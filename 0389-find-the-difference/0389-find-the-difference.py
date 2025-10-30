from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        frequencydict : dict = Counter(t)
        for char in s:
            frequencydict[char] -= 1
            if frequencydict[char] <= 0:
                del frequencydict[char]
        return list(frequencydict.keys())[0]