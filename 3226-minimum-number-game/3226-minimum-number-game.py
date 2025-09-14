class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # Empty array.
        arr : list = []
        if len(nums) == 0:
            return arr
        
        # Now.
        nums.sort(reverse = True)
        while len(nums) is not 0:
            AliceElement : int = nums.pop()
            BobElement : int = nums.pop()

            arr.append(BobElement)
            arr.append(AliceElement)
        return arr