class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Given is a integer array nums so i am assuming we even take negative numbers.
        ## As inputs we are given an integer array nums, two integers named indexdiff and valuediff.
        

        ## We have to get two indices that are different and the difference is equal to or same as the indexDiff integer that they gave.
        
        ## And the value difference also should be like equal or less to the ValueDiff.

        # Let me first try to solve this in BruteForce.
        ## Update : BruteForce worked.
        '''
        Our code has to obey the 3 rules of the question.
        1) i != j
        2) abs(i - j) <= indexDiff
        3) abs(nums[i] - nums[j]) <= valueDiff
        '''
        # Slding window with hashmap.

        ## Apparently we do sliding window with sortinglist and binary search.
        from sortedcontainers import SortedList

        window : list = SortedList()
        for idx , num in enumerate(nums):
            pos = window.bisect_left(num - valueDiff)

            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True
            
            window.add(num)

            if idx >= indexDiff:
                window.remove(nums[idx - indexDiff])
        return False

