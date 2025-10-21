class Solution:
    def scoreOfString(self, s: str) -> int:
       # Lets calculate the score in O(N) pass.

       score : int = 0
       for idx in range(len(s) - 1):
            score += abs(ord(s[idx]) - ord(s[idx + 1]))
       return score