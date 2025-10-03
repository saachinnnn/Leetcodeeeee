class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Now lets type the solution that i have written on my notebook.
        if len(nums) <= 0:
            return -1
        
        low , high = 0 , len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid 

            elif nums[mid] > target:
                high = mid - 1
            
            else:
                low = mid + 1
        return -1