class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans : list = []
        for i in range(numRows):
            val = 1
            row = []
            for j in range(i + 1):
                row.append(val)
                val = val * (i - j) // (j + 1)
            ans.append(row)
        return ans