class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # We can do this in O(N) pass using the insert function.
        flag = False
        for idx,value in enumerate(arr):
            if flag == True:
                flag = False
                continue
            if value == 0 and flag == False:
                arr.insert(idx + 1,0)
                flag = True
                arr.pop()
        return arr