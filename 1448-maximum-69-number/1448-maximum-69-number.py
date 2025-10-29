class Solution:
    def maximum69Number (self, num: int) -> int:
        # Mate these question names my god who makes them man lmfao.
        if num == 0:
            return 0 # The testcase that will never be asked lmfao.
        
        templist : list = list(str(num))
        for idx,num in enumerate(templist):
            if num == '6':
                templist[idx] = '9'
                break
        return int(''.join(templist))
