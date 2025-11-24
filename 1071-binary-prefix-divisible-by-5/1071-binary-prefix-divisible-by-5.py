class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        binarystring = ""
        ans = [False]*len(nums)
        for idx,ch in enumerate(nums):
            binarystring += str(ch)
            if int(binarystring,2) % 5 == 0:
                    ans[idx] = True
        return ans