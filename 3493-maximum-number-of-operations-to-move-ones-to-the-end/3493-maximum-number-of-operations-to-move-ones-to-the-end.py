class Solution:
    def maxOperations(self, s: str) -> int:
        Total = 0
        count = 0
        for idx in range(len(s)):
            if s[idx] == '1':
                if idx + 1 < len(s) and s[idx + 1] == '0':
                    count += 1
                    Total += count
                else:
                    count += 1
        return Total
