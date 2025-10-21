class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Starting case.
        if len(s) < k:
            return s[::-1] 
        elif len(s) >= k and len(s) < 2*k:
            reverse_list : list = list(s[:k][::-1]) + list(s[k:])
            return "".join(reverse_list)
        reverse_list : list = list(s)
        iterator : int = 0
        while iterator < len(s):
            reverse_list[iterator:iterator + k] = reverse_list[iterator:iterator + k][::-1]
            iterator += 2*k
        return "".join(reverse_list)
