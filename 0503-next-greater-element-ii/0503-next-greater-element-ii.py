class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # What if I just scale the array into twice the size.
        n = len(nums)
        stack : list = []
        ansarray : list = [0]*n
        for idx in range((2*n) - 1,-1,-1):
            while stack and nums[idx%n] >= stack[-1]:
                stack.pop()
            if not stack:
                ansarray[idx%n] = -1
            else:
                ansarray[idx%n] = stack[-1]
            stack.append(nums[idx%n])
        return ansarray[:n]

        