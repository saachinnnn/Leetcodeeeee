class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
           # I found it out but made a slight mistake.
           nums.sort()
           if not nums:
                return 0
           left = 0
           right = len(nums) - 1
           count = 0
           while left < right:
                if nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
           return count
