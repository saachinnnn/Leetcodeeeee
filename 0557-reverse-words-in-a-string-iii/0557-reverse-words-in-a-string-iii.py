class Solution:
    def reverseWords(self, s: str) -> str:
        List_string : list = s.split(" ")
        for idx in range(len(List_string)):
            List_string[idx] = List_string[idx][::-1]
        return " ".join(List_string)