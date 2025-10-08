class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Slightly different to Finding Peak Element problem.

        # Edge cases.
        if len(arr) == 0:
            return -1
        
        if len(arr) == 1:
            return 0
        

        # Now that are are done with the testcases.

        low , high = 0 , len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2

            # Now.
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1
            
            elif arr[mid - 1] > arr[mid]:
                high = mid - 1
        return low 