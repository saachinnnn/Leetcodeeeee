class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stones.count(char) if char in stones else 0 for char in set(jewels))