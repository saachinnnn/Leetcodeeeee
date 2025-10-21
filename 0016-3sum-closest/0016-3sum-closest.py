class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    return target
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest