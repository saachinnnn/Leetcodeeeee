from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Using Monotonic stack we can maintain the maximum element.
        MaxQueue : list = deque()

        result : list = []

        for i in range(len(nums)):
            # To see if the element is out of the window or not.
            if MaxQueue and MaxQueue[0] < i - k + 1:
                MaxQueue.popleft()
            
            # Now to remove the smaller elements before the current champion element.
            while MaxQueue and nums[MaxQueue[-1]] < nums[i]:
                MaxQueue.pop()
            
            # Now Append the current element.
            MaxQueue.append(i)

            # Now finally Check if the window is formed.
            if i >= k - 1:
                result.append(nums[MaxQueue[0]])
        return result