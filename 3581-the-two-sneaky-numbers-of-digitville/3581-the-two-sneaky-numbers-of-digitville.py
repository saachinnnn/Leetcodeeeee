class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Easyyyyyy.
        if not nums:
            return []
        ansarray : list = []
        Hashset : set = set()
        for num in nums:
            if num not in Hashset:
                Hashset.add(num)
            else:
                ansarray.append(num)
        return ansarray