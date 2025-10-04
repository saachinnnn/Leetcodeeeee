class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 0:
            return -1
        

        low , high = 0 , len(nums) - 1
        mid = 0
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] > nums[-1]:
                low = mid + 1
            
            elif nums[mid] < nums[-1]:
                high = mid - 1
            else:
                high = mid - 1
        pivot = low
        l , r = 0 , len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            realmid = (mid + pivot) % len(nums)
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
