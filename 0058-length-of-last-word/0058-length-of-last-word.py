class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        List_string : list = s.split(" ")
        return len(List_string[-1].strip())