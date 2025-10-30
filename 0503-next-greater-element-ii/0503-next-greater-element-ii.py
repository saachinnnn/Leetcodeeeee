class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # What if I just scale the array into twice the size.
        n = len(nums)
        nums = nums + nums
        stack : list = []
        ansarray : list = [0]*len(nums)
        for idx in range(len(nums) - 1,-1,-1):
            while stack and nums[idx] >= stack[-1]:
                stack.pop()
            if not stack:
                ansarray[idx] = -1
            else:
                ansarray[idx] = stack[-1]
            stack.append(nums[idx])
        return ansarray[:n]

        