class Solution:
    def smallestNumber(self, n: int) -> int:
        while n:
            if '0' not in bin(n)[2:]:
                return n
            n += 1
