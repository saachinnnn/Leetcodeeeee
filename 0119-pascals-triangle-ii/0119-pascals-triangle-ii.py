class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans : list = []
        for i in range(rowIndex + 1):
            val = 1
            row : list = []
            for j in range(i + 1):
                row.append(val)
                val = val * (i - j) // (j + 1)
            ans.append(row)
        return ans[rowIndex]