class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth : int = 0
        for customer in accounts:
            currentwealth = sum(customer)
            maxwealth = max(maxwealth,currentwealth)
        return maxwealth