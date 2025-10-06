class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set : set = set(jewels)

        count : int = 0
        for char in jewels_set:
            if char in stones:
                count += stones.count(char)
        return count  