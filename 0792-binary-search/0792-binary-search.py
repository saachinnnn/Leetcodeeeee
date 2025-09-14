class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) is 0:
            return -1
        elif len(nums) is 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        low : int = 0
        high : int = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1