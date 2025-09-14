class Solution:
    def countDigits(self, num: int) -> int:
        # Simplest way is to maintain a list.
        if num is 0:
            return 0
        TemporaryList : list = list(str(num))
        count : int = 0
        for number in TemporaryList:
                if num % int(number) == 0:
                    count += 1
        return count