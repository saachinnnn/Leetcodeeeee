# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # If I create an array the memory gets execeeded.
        ## If i run O(N) solution it gets TLE due to frequent Function Calls.

        # So.....

        ## Lemme try to implement binary search from scratch.
        if n == 1:
            return 1 if isBadVersion(n) else 0
        low_product , high_product = 1 , n

        while low_product <= high_product:
            middle_product = low_product + (high_product - low_product) // 2
            if isBadVersion(middle_product) and not isBadVersion(middle_product - 1) :
                return middle_product
            elif isBadVersion(middle_product) and isBadVersion(middle_product - 1):
                high_product = middle_product
            else:
                low_product = middle_product + 1
        return 0
        
