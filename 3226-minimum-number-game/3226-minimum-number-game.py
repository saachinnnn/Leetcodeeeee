class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # Empty array named as 'arr'
        arr : list = []
        if len(nums) == 0:
            return arr
        while len(nums) is not 0:
            index = nums.index(min(nums))
            AliceElement : int = nums.pop(index)
            arr.append(min(nums))
            nums.remove(min(nums))
            arr.append(AliceElement)
        return arr
           