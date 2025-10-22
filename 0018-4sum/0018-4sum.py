class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Forsum.(who even keeps these names dawg)
        ## Will try a 3sum modified approach.
        nums.sort()
        if not nums:
            return [] # Edge case.
        indexlist = []
        for idx in range(len(nums)- 3):
            for jdx in range(idx + 1,len(nums) - 2):
                left = jdx + 1
                right = len(nums) - 1
                while left < right:
                    currsum = nums[idx] + nums[jdx] + nums[left] + nums[right]
                    if currsum == target:
                        if [nums[idx],nums[jdx],nums[left],nums[right]] not in indexlist:
                            indexlist.append([nums[idx],nums[jdx],nums[left],nums[right]])
                        left += 1
                    elif currsum > target:
                        right -= 1
                    else:
                        left += 1
        return indexlist