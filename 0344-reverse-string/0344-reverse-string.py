class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        idx = 0
        while idx < (len(s) // 2):
            s[idx] , s[len(s) - idx - 1] = s[len(s) - idx - 1] , s[idx]
            idx += 1
        
