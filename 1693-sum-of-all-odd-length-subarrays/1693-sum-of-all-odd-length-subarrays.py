class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # Since its all positive numbers.

        # Edge cases.
        if len(arr) == 0:
            return 0
        
        ResultSum : int = sum(arr) # The final answer.

        oddidx : int = 3
        if oddidx > len(arr):
            return ResultSum
        
        # Now getting the PrefixSum array.
        PrefixSum : list = [0]*len(arr)
        PrefixSum[0] = arr[0]

        for i in range(1,len(arr)):
            PrefixSum[i] = PrefixSum[i - 1] + arr[i]
        
        while oddidx:
            for i in range(len(PrefixSum)):
                if (i + oddidx - 1) < len(arr):
                    ResultSum += PrefixSum[i + oddidx - 1] - (PrefixSum[i - 1] if i > 0 else 0)
                else:
                    break
            oddidx += 2
            if oddidx > len(PrefixSum):
                oddidx = 0
        return ResultSum
