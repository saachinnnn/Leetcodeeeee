class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if not colors or not neededTime:
            return 0
        prev_high = neededTime[0]
        maxcolors = 0
        for idx in range(1,len(colors)):
            if colors[idx] == colors[idx - 1]:
                maxcolors += min(neededTime[idx],prev_high)

                prev_high = max(neededTime[idx],prev_high)
            else:
                prev_high = neededTime[idx]
        return maxcolors