class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Easyyyyyy.
        if not nums:
            return []
        ansarray : list = []
        Hashset : set = set()
        for num in nums:
            if num in Hashset: # Always place the condition as the top criteria please.
                ansarray.append(num)
            Hashset.add(num)
        return ansarray