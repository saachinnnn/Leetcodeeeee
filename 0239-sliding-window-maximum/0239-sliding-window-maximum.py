from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq : list = deque()

        answer : list = []

        for i in range(len(nums)):
            # Now we have to check if the current greatest champion is expired or not.
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Now we hv to remove the smaller elements from the back.
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Now we append the index of the current element.
            dq.append(i)

            # Now we wait till the formation of the window and then we append the max element.

            if i >= k - 1:
                answer.append(nums[dq[0]])
        return answer