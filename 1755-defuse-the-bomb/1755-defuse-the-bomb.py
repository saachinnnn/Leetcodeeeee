class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # Hahaha another easy af question damn.
        if not code:
            return []
        if k == 0:
            return [0]*len(code)
        elif k > 0:
            ansarray : list = [0]*len(code)
            for idx in range(len(code)):
                iterator : int = (idx + 1) % len(code)
                sum : int = 0
                s = k
                while s != 0:
                    sum += code[iterator]
                    iterator += 1
                    if iterator >= len(code):
                        iterator = iterator % len(code)
                    s -= 1
                ansarray[idx] = sum
            return ansarray
        # Similarly...
        else:
            ansarray : list = [0]*len(code)
            for idx in range(len(code) - 1,-1,-1):
                iterator = idx - 1
                if iterator < 0:
                    iterator = len(code) - 1
                sum : int = 0
                s = k
                while s != 0:
                    sum += code[iterator]
                    iterator -= 1
                    if iterator < 0:
                        iterator = len(code) - 1
                    s += 1
                ansarray[idx] = sum
            return ansarray


