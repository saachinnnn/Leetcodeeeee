class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # The simplest answer is just to return 'low'
        low , high = 0 , len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                high = mid - 1
            
            else:
                low = mid + 1
            
        return low