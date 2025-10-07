class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       if len(nums) <= 0:
            return -1
       
       if len(nums) == 1:
            return 0

        # The above are the edgecases.

       low , high = 0 , len(nums) - 1

       while low <= high:
            mid = low + (high - low) // 2

            if low == high:
                return low
            if nums[mid] < (nums[mid + 1]):
                low = mid + 1
            elif nums[mid] > (nums[mid + 1]):
                high = mid
            
       return -1
