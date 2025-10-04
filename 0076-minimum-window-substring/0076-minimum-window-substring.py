from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) <= 0:
            return ""

        answers_substring : str = ""
        left : int = 0
        required : dict = Counter(t)
        checking : dict = Counter()

        minlength = float('inf')
        for right in range(len(s)):
            checking[s[right]] += 1
            while all(checking[char] >= required[char] for char in required):
                if minlength > (right - left + 1):
                    answers_substring = s[left:right + 1]
                    minlength = right - left + 1
                checking[s[left]] -= 1
                left += 1
        return answers_substring
                