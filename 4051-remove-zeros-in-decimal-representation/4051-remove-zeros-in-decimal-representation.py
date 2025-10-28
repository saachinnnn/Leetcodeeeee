class Solution:
    def removeZeros(self, n: int) -> int:
        if n == 0:
            return 0
        
        number = str(n)
        ans_str : str = ""
        for num in number:
            if num != '0':
                ans_str += num
        return int(''.join(ans_str))