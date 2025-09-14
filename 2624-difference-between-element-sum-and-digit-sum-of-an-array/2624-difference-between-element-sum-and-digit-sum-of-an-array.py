class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # Edge case.
        if len(nums) is 0:
            return 0
        
        ElementSum : int = sum(nums)
        DigitSum : int = 0
        for num in nums:
            Temp : list = list(str(num))
            DigitSum += sum(int(i) for i in Temp)
        return abs(ElementSum - DigitSum)