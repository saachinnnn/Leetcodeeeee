from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic stack solution.
        if not heights:
            return 0
        maxarea : int = 0
        stack : List[int] = []
        for idx in range(len(heights) + 1):
            curr_height = heights[idx] if idx < len(heights) else 0
            while stack and curr_height < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = idx if not stack else idx - stack[-1] - 1
                maxarea = max(height*width,maxarea)
            stack.append(idx)
        return maxarea