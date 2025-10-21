class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Classic two pointer approach.
        left : int = 0
        right : int = len(s) - 1

        temp : list = list(s)
        while left < right:
            if (temp[left].lower()).isalpha() and (temp[right].lower()).isalpha():
                temp[left] , temp[right] = temp[right] , temp[left]
                left +=1
                right -= 1
            elif temp[left].isalpha() == False:
                left +=1 
            else:
                right -= 1
        return "".join(temp)