class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        if len(words) is 0:
            return ""
        for word in words:
            if word[::] == word[::-1]:
                return word
        return ""