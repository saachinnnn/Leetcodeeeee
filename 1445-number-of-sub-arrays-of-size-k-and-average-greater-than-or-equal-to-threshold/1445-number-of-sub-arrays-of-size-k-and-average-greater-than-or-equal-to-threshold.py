class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) <= 0:
            return 0
        
        count : int = 0
        window_sum : int = sum(arr[:k])
        
        if window_sum / k >= threshold:
            count += 1

        for right in range(k,len(arr)):
            window_sum = window_sum - arr[right - k] + arr[right]

            if window_sum / k >= threshold:
                count += 1
        return count