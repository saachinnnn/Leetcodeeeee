class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 2 or k == 5:
            return -1
        rem = 0
        for length in range(1,k + 1):
            rem = (1 + rem*10) % k
            if rem == 0:
                return length
        return -1