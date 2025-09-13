class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        array : list = []
        for i in range(len(nums) + 1):
            array.append(i)
        for num in array:
            if num not in nums:
                return num   