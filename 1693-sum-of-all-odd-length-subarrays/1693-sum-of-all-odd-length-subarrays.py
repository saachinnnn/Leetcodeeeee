class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # Solving it using the maths version...

        # There exists a way to calculate the number of subarrays that are possible.

        # Edge cases.
        if len(arr) < 0:
            return 0
        
        ResultSum : int = 0

        for i in range(len(arr)):
            TotalSubarrays : int = (i + 1) * (len(arr) - i)
            OddSubarrays : int = TotalSubarrays // 2
            if TotalSubarrays % 2 == 1:
                OddSubarrays += 1
            ResultSum += OddSubarrays * arr[i]
        return ResultSum

        ''' The formula for calculating the number of subarrays that are possible is (i + 1) * (n(length of the array) * i)
            This is crucial to solve this problem '''