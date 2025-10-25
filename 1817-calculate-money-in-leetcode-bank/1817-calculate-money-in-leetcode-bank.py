class Solution:
    def totalMoney(self, n: int) -> int:
        # Lets solve this with some math.
        weeks = n // 7
        remainingdays = n % 7

        total = 0
        for w in range(weeks):
            total += (7 * (w + 1)) + 21
        
        for d in range(remainingdays):
            total += (weeks + 1) + d
        return total