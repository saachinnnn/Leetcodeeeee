class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Two pointers problem after sorting the array.
        
        nums.sort()
        left_ptr = 0
        right_ptr = len(nums) - 1
        ans = 0
        while left_ptr < right_ptr:
            total = nums[left_ptr] + nums[right_ptr]
            if total == k:
                ans += 1
                left_ptr += 1
                right_ptr -= 1
            elif total < k:
                left_ptr += 1
            else:
                right_ptr -= 1
        return ans