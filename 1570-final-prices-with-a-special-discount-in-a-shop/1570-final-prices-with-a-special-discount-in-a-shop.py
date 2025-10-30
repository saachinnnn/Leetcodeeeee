class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Next Smaller Element Problem.
        ansarray : list = [0]*len(prices)
        stack : list = []
        for idx in range(len(prices) - 1,-1,-1):
            if idx == len(prices) - 1:
                ansarray[idx] = prices[idx]
            else:
                while stack and prices[idx] < stack[-1]:
                    stack.pop()
                if not stack:
                    ansarray[idx] = prices[idx]
                else:
                    ansarray[idx] = prices[idx] - stack[-1]
            stack.append(prices[idx])
        return ansarray