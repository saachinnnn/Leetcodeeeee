class Solution:
    def numSub(self, s: str) -> int:
        # Apparently this is solvable in one line.
        Total = 0
        ones = 1
        for idx in range(len(s)):
            if s[idx] == '1':
                if idx < len(s) - 1 and s[idx + 1] == '1':
                    Total += ones + 1
                    ones += 1
                else:
                    Total += 1
                    ones = 1
        return Total % (10**9 + 7)