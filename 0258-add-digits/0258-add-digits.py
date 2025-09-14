class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        while True:
            Temp : list = list(str(num))
            answer : int = sum(int(i) for i in Temp)
            if len(str(answer)) == 1:
                return answer
            else:
                num = answer