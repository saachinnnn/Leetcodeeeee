class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
       # Let me just start to solve this question in brute force method.
       ## Nah actually using a stack is much more easier.

        if not nums1 or not nums2:
            return []
        
        stack = []
        # Precomputing the next greater element stack.
        nge = []
        for idx in range(len(nums2) - 1,-1,-1):
            if idx == len(nums2) - 1:
                nge.append(-1)
                stack.append(nums2[idx]) # We append the element itself.
            else:
                while stack and nums2[idx] > stack[-1]:
                    stack.pop()
                if stack == []:
                    nge.append(-1)
                    stack.append(nums2[idx])
                else:
                    nge.append(stack[-1])
                    stack.append(nums2[idx])
        
        # Now.
        nge = nge[::-1]
        ans = []
        for element in nums1:
            index = nums2.index(element)
            ans.append(nge[index])
        return ans
       