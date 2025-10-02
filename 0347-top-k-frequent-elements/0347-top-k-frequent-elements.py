from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This is by far the easiest method.
        Freq : dict = Counter(nums)
        
        # Store the top k elements
        top_k : list = Freq.most_common(k)

        return [num1 for num1,num2 in top_k]