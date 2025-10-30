class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # So i will solve this one last time.
        ## Basically we use a monotonic stack here to check if the previous element is greater.
        # So....
        if not heights:
            return 0
        
        maxarea : int = 0
        stack : list = []
        for idx in range(len(heights) + 1): # This is to compute the value of the last rectangle as well.
            curr_height : int = heights[idx] if idx < len(heights) else 0 # For the last case.
            while stack and curr_height < heights[stack[-1]]:
                # Calculate the height and width of the previous rectangles then.
                height : int = heights[stack.pop()]
                width : int = idx if not stack else idx - stack[-1] - 1
                maxarea = max(maxarea,width * height)
            stack.append(idx)
        return maxarea
