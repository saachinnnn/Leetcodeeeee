class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # Solving in Linear time using the Mathematical Approach.
        n = len(arr)
        result = 0
        for i in range(n):
            total = (i + 1) * (n - i)
            odd_count = total // 2 + (total % 2)
            result += arr[i] * odd_count
        return result
        # The number of subarrays that include arr[i] is (i + 1) * (n - i)
        # We count how many of those have odd lengths and multiply by arr[i]