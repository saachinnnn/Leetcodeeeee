class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Brute force bubble sort.
        for i in range(len(heights) - 1):
            for j in range(i + 1,len(heights)):
                if heights[j] > heights[i]:
                    temp = names[j]
                    names[j] = names[i]
                    names[i] = temp
                    temp = heights[j]
                    heights[j] = heights[i]
                    heights[i] = temp
        return names