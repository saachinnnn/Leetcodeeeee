class Solution:
    def numSub(self, s: str) -> int:
        ones = 0
        Total = 0
        for ch in s:
            if ch == '1':
                ones += 1
            else:
                Total += (ones * (ones + 1)) // 2
                ones = 0
        # Final streak of '1's (if any)
        Total += (ones * (ones + 1)) // 2
        return Total % (10**9 + 7)