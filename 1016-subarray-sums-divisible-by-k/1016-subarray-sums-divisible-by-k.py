from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Ok so whatever is the remainder that is 0 is said to be a correct answer.
        # I have to somehow find a way to get those prefix values.
        ## Maybe by reordering it?

        # Edge case.
        if len(nums) <= 0:
            return 0
        
        Hashmap : dict = defaultdict(int)
        count : int = 0
        Hashmap[0] = 1
        Prefixsum = 0
        for num in nums:
            Prefixsum += num

            remainder : int = Prefixsum % k 

            if remainder < 0:
                remainder += k
            count += Hashmap[remainder]
            Hashmap[remainder] += 1
        return  count