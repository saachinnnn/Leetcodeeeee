class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum(int(str(n)[idx]) if idx % 2 == 0 else -int(str(n)[idx]) for idx in range(len(str(n))))