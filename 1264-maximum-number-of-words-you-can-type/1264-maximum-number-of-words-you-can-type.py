class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count : int = 0
        for word in list(text.split(" ")):
            Flag = False
            for letter in list(brokenLetters):
                if letter in word:
                    Flag = True
                    break
            if Flag == False:
                count += 1
        return count