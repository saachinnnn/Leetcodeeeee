from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Instead of appending the distance to the stack as well which makes things more complicated, we can calculate the distance directly.
        ## So...

        ans : List[int] = [0]*len(temperatures)
        stack : list = []
        for idx in range(len(temperatures) - 1,-1,-1):
            while stack and temperatures[idx] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans[idx] = stack[-1] - idx
            stack.append(idx)
        return ans
# In the above approach we compute the distance simply by saving the index of the element in stack and subtracting it with current index traversing through the loop so that we can get the distance for the answer.
## Thus that distance is updated with the answer array.
### Much simpler solution than what i did earlier but both works in the same time complexity.


# So its not essentialy to add the distance/span to the stack like we did with stock and span question earlier.