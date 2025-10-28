class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Using the optimal approach.

        ## Using a Next Greater Element Stack.

        if not nums1 or not nums2:
            return [] # Weird ahh edge case.
        
        nge_stk : list = [0]*len(nums2)
        stk : list = []
        for idx in range(len(nums2) - 1,-1,-1):
            if idx == len(nums2) - 1:
                nge_stk[idx] = -1
                stk.append(nums2[idx])
            else:
                while stk and nums2[idx] > stk[-1]:
                    stk.pop()
                if stk == []:
                    nge_stk[idx] = -1
                    stk.append(nums2[idx])
                else:
                    nge_stk[idx] = stk[-1]
                    stk.append(nums2[idx])
        # So we have computed the next greater stack above successfully!! sui!!!.
        index_map = {num: i for i, num in enumerate(nums2)}
        ans = []
        for element in nums1:
            index = index_map[element]
            ans.append(nge_stk[index])
        return ans

