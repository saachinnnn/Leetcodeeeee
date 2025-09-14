class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product : int = 1
        for num in nums:
            if num < 0:
                product *= -1
            elif num > 0:
                product *= 1
            else:
                return 0
        return product