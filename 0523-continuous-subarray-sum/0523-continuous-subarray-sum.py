class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Edge cases
        if len(nums) < 2:
            return False
        
        RemainderHashMap : dict = {0:-1}
        
        total : int = 0

        for idx,num in enumerate(nums):
            total += num
            remainder : int = total % k if k > 0 else total

            if remainder in RemainderHashMap:
                if idx - RemainderHashMap[remainder] >= 2:
                    return True
            else:
                RemainderHashMap[remainder] = idx
        return False
