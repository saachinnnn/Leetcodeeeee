class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if n == 0:
            return 0
        product : int = 1
        Temp : list = list(str(n))
        for num in Temp:
            product *= int(num)
        Sum : int = sum(int(i) for i in Temp)
        return product - Sum