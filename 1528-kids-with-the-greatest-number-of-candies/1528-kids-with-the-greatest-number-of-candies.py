class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # The brute force would be.
        if not candies:
            return []
        
        ansarray : list = [True]*len(candies)
        for child,candy in enumerate(candies):
            if max(candies) > candy + extraCandies:
                ansarray[child] = False
        return ansarray