class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        Singlesum : int = 0
        Doublesum : int = 0
        for num in nums:
            if len(str(num)) == 1:
                Singlesum += num
            else:
                Doublesum += num
        return not Singlesum == Doublesum